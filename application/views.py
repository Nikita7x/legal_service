from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework_xml.parsers import XMLParser
from .serializers import LegalTreeSerializer
from .utils import normalize_date, normalize_term


class LegalTreeView(APIView):
    parser_classes = [JSONParser, XMLParser]

    def post(self, request, format=None):
        serializer = LegalTreeSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            normalized_data = self.normalize_tree(data)
            return Response(normalized_data)
        return Response(serializer.errors, status=400)

    def normalize_tree(self, tree):
        for key, value in tree.items():
            if isinstance(value, str):
                if "дата" in key.lower():
                    tree[key] = normalize_date(value)
                elif "срок" in key.lower():
                    tree[key] = normalize_term(value)
            elif isinstance(value, dict):
                tree[key] = self.normalize_tree(value)
            elif isinstance(value, list):
                tree[key] = [self.normalize_tree(item) if isinstance(item, dict) else item for item in value]
        return tree