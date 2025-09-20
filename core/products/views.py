from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .documents import ProductsDocument


def index(request):
    return render(request, 'index.html')


class ProductsAPIView(APIView):
    def get(self, request):
        search = request.GET.get('search', '')
        
        if not search:
            return Response({
                'status': True,
                'message': 'No search query provided.',
                'data': []
            })
            
        products = []
        
        results = ProductsDocument.search().query(
            'multi_match',
            query=search,
            fields=['product_name', 'product_brand'],
            fuzziness='auto',
            operator='and',
            type='best_fields'
            
        ).extra(size=30)  # Limiting to 30 results for performance
        
        results = results.execute()
        
        for result in results:
            products.append({
                'id': result.id,
                'product_name': result.product_name,
                'product_brand': result.product_brand,
                'product_price': result.product_price,
            })
        
        return Response({
            'status': True,
            'message': 'Products fetched successfully.',
            'data': products
        }, status=status.HTTP_200_OK)