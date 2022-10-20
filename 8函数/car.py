def make_car(maker, model, **info):
    # 创建一个字典 存储汽车信息
    car_info = {}
    car_info['maker'] = maker
    car_info['model'] = model

    for key, value in info.items():
        car_info[key] = value

    return car_info


car = make_car('Tesla', 'model3', color='blue', two_package=True)
print(car)