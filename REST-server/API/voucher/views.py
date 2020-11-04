from django.shortcuts import render
from rest_framework import viewsets
from .models import Voucher, Product, Order, History
from .serializer import VoucherSerializer, ProductSerializer, OrderSerializer, HistorySerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime

class VoucherViewSet(viewsets.ModelViewSet):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

    @action(detail=False, methods=['PUT'])
    def verify(self, request):
        _id = request.data['id']
        Vobj=Voucher.objects.get(id=_id)
        if Vobj.capacity > 0:
            Vobj.staged = True  
            Vobj.save()
            return Response({'status': 'verify'})
    
        else:
            return Response({'status': 'not verify'})
    
    @action(detail=False, methods=['GET'])
    def unstage(self, request):
        Vobj=Voucher.objects.all()
        for obj in Vobj:
            obj.staged = False
            obj.save()
            
        return Response({'status': 'voucher unstaged'})



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False)
    def delete_all(self, request):
        Order.objects.all().delete()
        return Response("Success")
    
    @action(detail=False, methods=['GET'])
    def submit(self, request):
        Vobj = Voucher.objects.filter(staged=True)
        if len(Vobj) > 0:
            for obj in Vobj:
                obj.capacity = obj.capacity - 1
                obj.staged = False
                obj.save()
        

        orders = Order.objects.all()

        history = ""
        payout = []
        for i in orders:
            history += i.title + ","
            payout.append(i.price)

        payout = sum(payout)
        cdate = datetime.date(datetime.now())
        obj = History.objects.create(orders=history, payout=payout, date=cdate)

        Order.objects.all().delete()

        return Response("Order Transacted")

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


    