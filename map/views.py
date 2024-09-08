from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LocationData
from .forms import SearchForm, UploadFileForm
import pandas as pd

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            data = pd.read_excel(file)
            required_columns = ['application_id', 'loan_account_number', 'product', 'address', 'area_type', 'state', 'pincode', 'latitude', 'longitude']
            if not all(column in data.columns for column in required_columns):
                missing_columns = [column for column in required_columns if column not in data.columns]
                return HttpResponse(f'Missing columns in the uploaded file: {", ".join(missing_columns)}')

            for _, row in data.iterrows():
                LocationData.objects.create(
                    application_id=row['application_id'],
                    loan_account_number=row['loan_account_number'],
                    product=row['product'],
                    address=row['address'],
                    area_type=row['area_type'],
                    state=row['state'],
                    pincode=row['pincode'],
                    latitude=row['latitude'],
                    longitude=row['longitude']
                )
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def index(request):
    form = SearchForm(request.POST or None)
    locations = []
    
    if request.method == 'POST' and form.is_valid():
        pincode = form.cleaned_data.get("pincode")
        locations = LocationData.objects.filter(pincode=pincode)

        if not locations.exists():
            return HttpResponse("No locations found for this pincode")
    
    context = {
        'form': form,
        'locations': locations,
    }
    return render(request, 'index.html', context)

def pincode_search(request):
    form = SearchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pincode = form.cleaned_data.get("pincode")
        locations = LocationData.objects.filter(pincode=pincode)

        if locations.exists():
            location_data = [{
                'lat': loc.latitude,
                'lng': loc.longitude,
                'application_id': loc.application_id,
                'loan_account_number': loc.loan_account_number,
                'product': loc.product,
                'address': loc.address,
                'area_type': loc.area_type,
                'state': loc.state
            } for loc in locations]

            return render(request, 'index.html', {'form': form, 'locations': location_data, 'pincode': pincode})
        else:
            return HttpResponse("No locations found for this pincode")
  
    return render(request, 'index.html', {'form': form})

def clear_data(request):
    if request.method == 'POST':
        LocationData.objects.all().delete()
        return redirect('success')
    return render(request, 'clear_data.html')
