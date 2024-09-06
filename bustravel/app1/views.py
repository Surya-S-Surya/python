from django.shortcuts import render
from django.http import HttpResponse

from .models import BusDetails
from .forms import TicketForm

def book_ticket(request):
    if request.method=='POST':
        Busno=request.POST['busno']
        D=request.POST['d']
        Np=request.POST['np']

        busdetails=BusDetails.objects.get(busno=Busno)
        Dlist=busdetails.d.split(',')
        cost=busdetails.tc.split(',')

        i=Dlist.index(D)
        cost=cost[i]

        if int(Np)<=busdetails.sa:
            busdetails.sa=busdetails.sa-int(Np)
            busdetails.save()
            tot=int(Np)*cost
            return HttpResponse("Ticket booked total Cost:"+str(tot))
        else:
            return HttpResponse("Ticket not booked due to less seats ")

    return render(request,'ticket_booking.html',context={'form'=form})
