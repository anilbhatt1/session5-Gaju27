import math
import random
import time


def time_it(fn, *args, repetitons=1, **kwargs):
    if repetitons <= 0:
        raise ValueError("Repetions must be greater than 0 value")
    if fn == print:
        t1 = time.perf_counter()
        for p in range(repetitons):
            print(*args, **kwargs)
        t2 = time.perf_counter()
    elif fn == 'squared_power_list':
        t1 = time.perf_counter()
        output = squared_power_list(*args, **kwargs)
        t2 = time.perf_counter()
    elif fn == 'polygon_area':
        '''where
        s  is the length of any side
        n  is the number of sides
        tan  is the tangent function calculated in degrees
        time_it(polygon_area, 15, sides = 3, repetitons=10)'''
        t1 = time.perf_counter()
        output = polygon_area(*args, **kwargs)  # (s * s * n) / (4 * math.tan(180 / n))
        t2 = time.perf_counter()
    elif fn == 'temp_converter':
        t1 = time.perf_counter()
        output = temp_converter(*args, **kwargs)
        t2 = time.perf_counter()
    elif fn == 'speed_converter':
        t1 = time.perf_counter()
        output = speed_converter(*args, **kwargs)
        t2 = time.perf_counter()
    return ((t2 - t1) / repetitons, output)


def squared_power_list(*args, **kwargs):
    pvalue = args[0]
    if pvalue <= 0:
        raise ValueError("Please provide Power value must be greater than 0")
    start, end = kwargs.values()
    list_of_squares = [pvalue ** i for i in range(start, end + 1)]
    return list_of_squares


def polygon_area(*args, **kwargs):
    length = args[0]
    nsides = kwargs['sides']
    if nsides == 3:
        ''' Heron's Formula sometimes called Hero's formula
            Using which we can calculate area of triagle when 
            length of side knows to us '''
        s = (length + length + length) / 2
        area = math.sqrt(s * (s - length) * (s - length) * (s - length))

    elif nsides == 4:
        area = length * length
    elif nsides == 5:
        ''' when all the side length is equal
            divide the pentagon into five triagle
            draw a center line with 90degree
            base of triagle is half of the side length of pentagon
            hence angle of pentagon center is 36 degree (i.e 360/10=36)
            tan(36)=(pentagon_length/2)/adjacent
            adjacent= (pentagon_length/2)/tan(36)            
            area_triangle=1/2(base_of_triagle * adjacent)
            area_pentagon=10* area_triagle'''
        base_of_triangle = length / 2
        adjacent = base_of_triangle / math.tan(36)
        area_triangle = (base_of_triangle * adjacent) / 2
        area = 10 * area_triangle
    elif nsides == 6:
        # area = (length * length * nsides) / (4 * math.tan(180 / nsides))
        area = ((3 * math.sqrt(3)) / 2) * (length ** 2)
    else:
        raise ValueError("Must be in range of 3 to 6 .")
    return area


def temp_converter(*args, **kwargs):
    current_temp = args[0]
    input_temp, output_temp = kwargs.values()
    if input_temp == 'f':
        if output_temp == 'c':
            final_temp = (current_temp - 32) * (5 / 9)
        elif output_temp == 'k':  # k for kelvin
            final_temp = (current_temp - 32) * (5 / 9) + 273.15
        else:
            raise Exception("Not in any conversion key value must in 'c' or 'k' . ")
    elif input_temp == 'c':
        if output_temp == 'f':
            final_temp = (current_temp * 9 / 5) + 32
        elif output_temp == 'k':
            final_temp = current_temp + 273.15
        else:
            raise Exception("Not in any conversion key value must in 'f' or 'k' ")
    elif input_temp == 'k':
        if output_temp == 'c':
            final_temp = (current_temp - 273.15)
        elif output_temp == 'f':
            final_temp = (current_temp - 273.15) * (9 / 5) + 32
        else:
            raise Exception("Not in any conversion key value must in 'f' or 'c' ")
    else:
        raise Exception("Not in standard temperature input")
    return final_temp


def speed_converter(*args, **kwargs):
    speed_input = args[0]
    dist_in, time_in = kwargs.values()
    if dist_in == 'yard' and time_in == 'day':
        speed_out = speed_input * 26247
    elif dist_in == 'yard' and time_in == 'hr':
        speed_out = speed_input * 1094
    elif dist_in == 'yard' and time_in == 'min':
        speed_out = speed_input * 18.227
    elif dist_in == 'yard' and time_in == 's':
        speed_out = speed_input / 3.292
    elif dist_in == 'yard' and time_in == 'ms':
        speed_out = speed_input / 3292
    elif dist_in == 'km' and time_in == 'day':
        speed_out = speed_input * 24
    elif dist_in == 'km' and time_in == 'hr':
        speed_out = speed_input * 1
    elif dist_in == 'km' and time_in == 'min':
        speed_out = speed_input / 60
    elif dist_in == 'km' and time_in == 's':
        speed_out = speed_input / 3600
    elif dist_in == 'km' and time_in == 'ms':
        speed_out = speed_input / 3600000
    elif dist_in == 'm' and time_in == 'day':
        speed_out = speed_input * 24000
    elif dist_in == 'm' and time_in == 'hr':
        speed_out = speed_input * 1000
    elif dist_in == 'm' and time_in == 'min':
        speed_out = speed_input / 60
    elif dist_in == 'm' and time_in == 's':
        speed_out = speed_input / 3.6
    elif dist_in == 'm' and time_in == 'ms':
        speed_out = speed_input / 3600
    elif dist_in == 'ft' and time_in == 'day':
        speed_out = speed_input * 78740
    elif dist_in == 'ft' and time_in == 'hr':
        speed_out = speed_input * 3281
    elif dist_in == 'ft' and time_in == 'min':
        speed_out = speed_input * 54.681
    elif dist_in == 'ft' and time_in == 's':
        speed_out = speed_input / 1.097
    elif dist_in == 'ft' and time_in == 'ms':
        speed_out = speed_input / 1097
    else:
        raise Exception("Wrong speed converter format")
    return speed_out
