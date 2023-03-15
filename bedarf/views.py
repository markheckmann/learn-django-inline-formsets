from django.shortcuts import render, redirect
from django.views import View, generic
from django.views.generic.edit import DeleteView, CreateView
from .forms import BedarfForm, BedarfVZPFormset
from .models import Bedarf


class BedarfListView(generic.ListView):
    model = Bedarf
    template_name = "bedarf/bedarfList.html"


class BedarfCreateView(CreateView):
    model = Bedarf
    success_url = "/bedarf/"
    template_name = "bedarf/bedarfCreate.html"
    fields = "__all__"


class BedarfDeleteView(DeleteView):
    model = Bedarf
    success_url = "/bedarf/"
    template_name = "bedarf/bedarfDelete.html"


class BedarfView(View):
    def get(self, request):
        form = BedarfForm()
        context = {"form": form}
        return render(request, "bedarf/bedarf.html", context)

    def post(self, request):
        form = BedarfForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("bedarf")


class BedarfInlineView(View):
    def get(self, request, pk):
        instance = Bedarf.objects.get(id=pk)
        form_parent = BedarfForm(instance=instance, prefix="bedarf")
        formset_vzp = BedarfVZPFormset(instance=instance, prefix="bedarfvzp")
        context = {"form": form_parent, "formset": formset_vzp}
        return render(request, "bedarf/bedarfDetails.html", context)

    def post(self, request, pk):
        instance = Bedarf.objects.get(id=pk)
        form = BedarfForm(request.POST, instance=instance, prefix="bedarf")
        if form.is_valid():
            form.save()
        formset = BedarfVZPFormset(request.POST, instance=instance, prefix="bedarfvzp")
        if formset.is_valid():
            formset.save()
        return redirect("bedarf_details", pk=pk)
