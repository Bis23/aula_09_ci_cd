import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14
    
def teste_soma():
    # given a value 1 of 7 and a value 2 of 8
    value1 = 7
    value2 = 8
    
    # when we calculate the sum
    output = methods.soma(value1, value2)
    
    # then the result shoud be 15
    assert output == 15
    
def teste_subtracao():
    # given a value 1 of 9 and a value 2 of 6
    value1 = 9
    value2 = 6
    
    # when we calculate the sub
    output = methods.sub(value1,value2)
    
    # then the result should be 3
    assert output == 3
    
def teste_multiplicacao():
    # given a value 1 of 4 and a value 2 of 2
    value1 = 4
    value2 = 2
    
    # when we calculate the mult
    output = methods.mult(value1,value2)
    
    # then the result should be 8
    assert output == 8
    
def teste_divisao():
    # given a value 1 of 14 and a value 2 of 7
    value1 = 14
    value2 = 7
    
    # when we calculate the div
    output = methods.div(value1,value2)
    
    # then the result should be 2
    assert output == 2