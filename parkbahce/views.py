from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render

from .models import Park


def index(request):
    return render(request, "parkbahce/index.html")


def park_list(request):
    parklar = Park.objects.all()
    return render(request, "parkbahce/parklar/list.html", {"parklar": parklar})


# get by uuid
def park_detail(request, uuid):
    park = Park.objects.get(uuid=uuid)

    # Park geometrisini EPSG:5256'dan EPSG:4326'ya dönüştür
    if park.geom:
        # Geometriyi 5256 (TUREF) olarak ayarla
        park.geom.srid = 5256
        # WGS84 (4326) koordinat sistemine dönüştür
        park.geom.transform(4326)

    return render(request, "parkbahce/parklar/detail.html", {"park": park})


def park_edit(request, uuid):
    park = Park.objects.get(uuid=uuid)
    if request.method == "POST":
        park.name = request.POST.get("name")
        park.description = request.POST.get("description")
        park.save()
        return render(request, "parkbahce/parklar/detail.html", {"park": park})
    return render(request, "parkbahce/park_edit.html", {"park": park})


def park_delete(request, uuid):
    park = Park.objects.get(uuid=uuid)
    if request.method == "POST":
        park.delete()
        return render(
            request, "parkbahce/park_list.html", {"parklar": Park.objects.all()}
        )
    return render(request, "parkbahce/park_delete.html", {"park": park})
