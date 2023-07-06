from django.shortcuts import redirect, render, get_object_or_404
from apps.Worker.models import Worker
from apps.Company.models import Company
import plotly.graph_objs as go
from django.db.models import Count


def dashboard(request):

    return render(request, 'dashboard.html')
