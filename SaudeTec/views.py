from django.shortcuts import render, redirect
from django.views import View
from .models import Ficha_Pre_Consulta

class CheckListView(View):
    def get(self, request):
        return render(request, 'checklist.html')

    def post(self, request):
        motivo = request.POST.get("motivo")
        periodo = request.POST.get("periodo")
        dor = request.POST.get("dor")
        quando_dor = request.POST.get("quando_dor")
        algo_mais = request.POST.get("algo_mais")

        ficha_pre_consulta = Ficha_Pre_Consulta(
            motivo = motivo
            periodo = periodo
            dor = dor
            quando_dor = quando_dor
            algo_mais = algo_mais
        )

        ficha_pre_consulta.save()

        return redirect('SaudeTec:home')