from django.http import JsonResponse

from django.views.generic import View
    
class Species(View):
    #template_name = 'home.html'
    def get(self,request,*args,**kwargs):
        ''
        #print('here')
        data = [35,35.8,8,39,30,31,31,31,33,25]
        return JsonResponse({'message':data})
    