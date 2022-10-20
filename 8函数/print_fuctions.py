def show_unprinted(unprinted_designs, completed_models):
    # 模拟打印每个设计，直到没有未打印的设计为止
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计制作3D打印模型过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def printed_models(completed_models):
    # 显示已经打印好的模型
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print('\t' + completed_model)
