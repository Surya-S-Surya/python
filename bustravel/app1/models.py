from django.db import models

class BusDetails(models.Model):
    busno = models.CharField(max_length=20)
    dt = models.DateTimeField()
    d = models.CharField(max_length=200)
    sa = models.IntegerField()
    tc = models.CharField(max_length=200)

BusDetails.objects.create(busno='1',dt='2023-12-01 08:00:00',d='a,b,c',sa=10,tc='50,100,150')
BusDetails.objects.create(busno='2',dt='2023-12-02 08:00:00',d='l,m,n',sa=10,tc='50,100,150')
BusDetails.objects.create(busno='3',dt='2023-12-03 08:00:00',d='x,y,z',sa=10,tc='50,100,150')
