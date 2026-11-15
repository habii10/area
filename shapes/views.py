from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads


# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class SquareView(View):
    def post(self,request):

        json_data=request.body

        form_data=loads(json_data)

        a=form_data.get("side")       

        result=a**2

        response_data={"square-result":result} 

        return JsonResponse(response_data) 
    
@method_decorator(csrf_exempt,name="dispatch")
class RectangleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        l=form_data.get("length")  
        w=form_data.get("width")
        result=l*w
        response_data={"area_rectangle":result}
        return JsonResponse(response_data)

@method_decorator(csrf_exempt,name="dispatch")
class TriangleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        b=form_data.get("base")  
        h=form_data.get("height")
        result=0.5*b*h
        response_data={"area_triangle":result}
        return JsonResponse(response_data)    


@method_decorator(csrf_exempt,name="dispatch")
class circleView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        r=form_data.get("radius")
        result=3.14*r*r
        response_data={"area_circle":result}
        return JsonResponse(response_data)    

@method_decorator(csrf_exempt,name="dispatch")
class ParellelogramView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        b=form_data.get("base")
        h=form_data.get("height")
        result=b*h
        response_data={"area_parellelogram":result}
        return JsonResponse(response_data)    

@method_decorator(csrf_exempt,name="dispatch")
class TrapeziumView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        a=form_data.get("first")
        b=form_data.get("second")
        h=form_data.get("height")
        result=0.5*(a+b)*h
        response_data={"area_trapezium":result}
        return JsonResponse(response_data)   

@method_decorator(csrf_exempt,name="dispatch")
class RhombusView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        d1=form_data.get("diagonal1")
        d2=form_data.get("diagonal2")
        result=0.5*d1*d2
        response_data={"area_rhombus":result}
        return JsonResponse(response_data)            

@method_decorator(csrf_exempt,name="dispatch")
class ElipseView(View):
    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        a=form_data.get("axis1")
        b=form_data.get("axis2")
        result=3.14*a*b
        response_data={"area_ellipse":result}
        return JsonResponse(response_data)                


