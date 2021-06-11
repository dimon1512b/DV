import json

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import logging.config
# from .logging_conf import LOGGING
from .models import Cars

# logging.config.dictConfig(LOGGING)
# logger = logging.getLogger('views')
from .utils import serialize, castom_paginate, smart_search_def

data_brand = set()
data_model = set()
data_transmission = set()
data_region = set()
data_city = set()
data_engine_type = set()
data_drive_type = set()
data_year = set()
data_engine_capacity = set()
data_body_type = set()
data_description = dict()

for obj in Cars.objects.all():
	data_brand.add(obj.brand)
	data_model.add(obj.model)
	data_transmission.add(obj.transmission)
	data_region.add(obj.region)
	data_city.add(obj.city)
	data_engine_type.add(obj.engine_type)
	data_body_type.add(obj.body_type)
	data_drive_type.add(obj.drive_type)
	data_year.add(obj.year)
	data_engine_capacity.add(obj.engine_capacity)
	data_description[obj.id] = obj.description

data_filter = {'brand': list(data_brand),
               'model': sorted(list(data_model)),
               'transmission': list(data_transmission),
               'region': sorted(list(data_region)),
               'city': sorted(list(data_city)),
               'engine_type': list(data_engine_type),
               'body_type': list(data_body_type),
               'drive_type': list(data_drive_type),
               'year': sorted(list(data_year)),
               'engine_capacity': sorted(list(data_engine_capacity)),
               'search_request': data_description}


# logger.info(f'data_filter = {data_filter}')

def ajax_get_cars(request):
	print('request =====', request)
	print('request.GET =====', request.GET)
	print('request.GET.get("body_type") =====', request.GET.get('body_type'))
	for i in data_filter:
		print(f'Параметр который проверяем: {i}')
		try:
			if request.GET.get(i):
				# logger.info('filter def get(i)')
				print('It was return filters')
				return filters(request)
		except Exception as error:
			raise Exception(f'Ошибка в переборе параметров реквеста {error}')
	cars = Cars.objects.all()
	count_obj_on_page = 5
	len_cars = len(cars)
	index_ = 0
	data_cars = castom_paginate(cars, count_obj_on_page)
	if 'page' in request.GET:
		index_ = int(request.GET.get('page')) - 1
	print('We before dict_ in base def!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n\n'
	      '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
	dict_ = {
		'auto': data_cars[index_],
		'all_data_types': data_filter,
		'pages': len(data_cars),
		'current_page': index_ + 1
	}
	print('We ready to do return in base def!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n\n'
	      '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
	print('DESCRIPTIONS//////////////////////////////////////////////////', data_filter['search_request'])
	return HttpResponse(json.dumps(dict_))


def filters(request):
	# full_path = HttpRequest.get_full_path(request)
	request_get = request.GET
	filter = Cars.objects.all()
	for param in request_get:
		# print('PARAM IS', param)
		# print('PARAM TYPE IS', type(param))
		# print('request.GET.get(PARAM) IS', request.GET.get(param))
		# print('request.GET.get(PARAM) TYPE IS', type(request.GET.get(param)))
		if param == 'body_type':
			# print('param is body_type')
			# print('request.GET.get(param) =', request.GET.get(param))
			# print('type(request.GET.get(param)) =', type(request.GET.get(param)))
			if request_get.get(param) != '':
				# print('-----request_get.get(param) != ""-----')
				filter = filter.filter(body_type=request_get.get(param))
			continue
		elif param == 'brand':
			if request_get.get(param) != '':
				filter = filter.filter(brand=request_get.get(param))
			continue
		elif param == 'model':
			if request_get.get(param) != '':
				filter = filter.filter(model=request_get.get(param))
			continue
		elif param == 'search_request':
			if request_get.get(param) != '':
				filter = smart_search_def(filter, data_description, request_get.get(param))
			continue
	print('ОТФИЛЬТРОВАННЫЙ МАССИВ ЭТО !!!!', filter)
	count_obj_on_page = 5
	len_cars = len(filter)
	if filter:
		index_ = 0
		data_cars = castom_paginate(filter, count_obj_on_page)
		if 'page' in request.GET:
			index_ = int(request.GET.get('page')) - 1
		print('INDEX_==========================', index_)
		print('DATA_CARS ==========================', data_cars)
		print('DATA_CARS[INDEX] =======================', data_cars[index_])
		dict_ = {
			'auto': data_cars[index_],
			'all_data_types': data_filter,
			'pages': len(data_cars),
			'current_page': index_ + 1
		}
		print('DICT!!!!!!!!!!', dict_)
		return HttpResponse(json.dumps(dict_))
	else:
		dict_ = {
			'auto': [],
			'all_data_types': data_filter,
			'pages': 0,
			'current_page': 0
		}
		print('DICT!!!!!!!!!!', dict_)
		return HttpResponse(json.dumps(dict_))


def base_page(request):
	# logger.info('base_page def')
	# logger.info(f'REQUEST IS {request}')
	# logger.info(f'REQUEST IS {request.GET}')
	# full_path = HttpRequest.get_full_path(request)
	# logger.info(f'full_path {full_path}')
	data = Cars.objects.order_by('date_created')
	paginator = Paginator(data, 20)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)  # Ссылка на конкретную страницу пагинатора
	for i in data_filter:
		if request.GET.get(i):
			# logger.info('filter def get(i)')
			return filters(request)
	if (request.GET.get('price_from') not in ('', None)) or (request.GET.get('price_to') not in ('', None)):
		# logger.info('filter def price')
		# logger.info(request.GET.get('price_from'))
		# logger.info(request.GET.get('price_to '))
		return filters(request)
	else:
		return render(request, 'cars/base.html', {
			'data': page_obj.object_list,
			'page_obj': page_obj,
			'data_filter': data_filter,
			'request': request.GET,
			'full_path': full_path})


def detail_car(request, id):
	# logger.info('detail_car def')
	car = Cars.objects.get(pk=id)
	# logger.info(f'it is request: ===>>> {request}')
	# logger.info(f'it is type request: ===>>> {type(request)}')
	# logger.info(f'it is request.GET: ===>>> {request.GET}')
	# logger.info(f'it is id: ===>>> {id}')
	# logger.info(f'it is type id: ===>>> {type(id)}')
	return render(request, 'cars/cars_list.html', {'el': car, 'data_filter': data_filter})

# class BasePage(ListView):

# model = Cars
# template_name = 'cars/base.html'
# context_object_name = 'data'
# paginate_by = 10

# def get_queryset(self):
# return Cars.objects.order_by('date_created')
# def show_page(self):
# data = Cars.objects.order_by('date_created')
# return render(self, 'cars/base.html', {'data': data})


# class CarDetailView(DetailView):

# model = Cars
# context_object_name = 'el'
# template_name = 'cars/cars_list.html'
