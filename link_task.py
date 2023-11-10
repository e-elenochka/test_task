import math

def formula(coord):
    split_list = coord.lower().split()
    num_list = [int(num) for num in filter(
        lambda num: num.isnumeric(), split_list)]
    
    try:
        if split_list[0] == 'square':
            s_num = num_list[0] * num_list[1]
            p_num = num_list[2] * 4
            return (f'Square Perimeter {p_num:.2f} Area {s_num:.2f}')

        if split_list[0] == 'rectangle':
            a = num_list[0] - num_list[2]
            b = num_list[1] - num_list[3]
            s_num = a*b
            p_num = (a+b)*2
            return (f'Rectangle Perimeter {p_num:.2f} Area {s_num:.2f}')

        if split_list[0] == 'circle':
            p_num = 2 * math.pi * num_list[2]
            s_num = math.pi * math.pow(num_list[2], 2)
            return (f'Circle Perimeter {p_num:.2f} Area {s_num:.2f}')
        

    except Exception:
        print(f'Enter the data correctly')


if __name__ == '__main__':
    coord = str(input('Enter the coordinates: ')).lower()
    print(formula(coord))

            




