import math
PI=math.pi
def square_root(x):
    return x**0.5
print("------------------------------AI CHATBOT INITIALIZED--------------------------------")
print("I can understand the natural language requests to claculate the properties of 3d shapes(frustum,Sphere,Cube,Cuboid,Cylinder,Cone,Hemisphere).")
print("----------------------------------------------------------------------")
command=input("AI: Hey! I am your 3D geometry AI Asisstent.Which property do you want to calculate today? ").lower()
valid_shapes=["cube","cuboid","cylinder",'frustum',"cone","hemisphere","sphere"]
shape_choice=input("Enter the 3D shape that you need to calculate: ").strip().lower()
if shape_choice not in valid_shapes:
    print("AI Error:shape is not recognised.Please enter the shape from valid_shapes")
elif shape_choice=="cube":
    print("AI:You enterd cube!")
    while True:
        try:
            s=float(input("Enter the side of the cube: "))#s denotes the side of the cube that need to be entered
            if s<=0:
                print("AI Error:the side of the cube cannot be less than or equal to zero.please enter the correct vlaue of side")
            else:
                break
        except ValueError:
                print("AI Error:You entered the digit in letters.Please type a number(like 5),not words!")
    if "total edge length" in command or 'tel'in command:
        total_edge_length=12*s
        print("AI Result:The total edge length of the cube is: ",total_edge_length)
    elif "area of one face" in command:
        a=s*s
        print("AI Result:The area of one face is: ",a)
    elif "perimeter of one face" in command or 'p' in command:
        p=4*s
        print("AI Result:the perimeter of one face of the cuboid is: ",p)
    elif "lateral surface area"in command or "lsa" in command:
        l_s_a=4*(s**2)
        print("AI Result:the lateral surface area of the cube: ",l_s_a)
    elif "total surface area"in command or  "tsa" in command:
        t_s_a=6*(s**2)
        print("AI Result:The total surface area of the cube is: ",t_s_a)
    elif "legth of face diagonal"in command or "lfd" in command:
        l_f_d=s*(2**0.5)
        print("AI Result:The length of face diagonal is: ",l_f_d)
    elif "length of body diagonal"in command or "lbd" in command:
        l_b_d=s*(3**0.5)
        print('AI Result:the length of body diagonal of the cube is: ',l_b_d)
    elif 'volume' in command or 'v' in command:
        v=s**3
        print('AI Result:The volume of the cube is: ',v)
    else:
        print("AI Error:Sorry,I am only trained to calculate the properties like total edge length,area of one face,perimeter of one face,total surface area,lateral surface area,volume,length of body digonal and face diagonal.")
    input('Please press Enter button to exit')    
elif shape_choice=="cuboid":
    print("AI:you entered cuboid")
    while True:
        try:
            l=float(input("Enter the length of the cuboid: "))
            b=float(input("Enter the breadth of the cuboid: "))
            h=float(input("Enter the height of the cuboid: "))
            if l<=0 or b<=0 or h<=0:
                    print("AI Error:The length,breadth or height of any 3D shapes cannot be less than or equal to zero.Please enter the appropriate positive value.")
            else:
                break
        except ValueError:
            print("AI Error:You entered the digit in letters.Please type a number(like 5),not words!")
    if "total edge length"in command or "sum of all edges" in command:
        total_edge_length=4*(l+b+h)
        print("AI Result:the total edge length of the cuboid is: ",total_edge_length)
    elif "total surface area"in command or "tsa" in command:
        total_surface_area=2*(l*b+b*h+h*l)
        print("AI Result:The total surface area of the cuboid is: ",total_surface_area)
    elif "lateral_surface_area"in command or "lsa" in command:
        lateral_surface_area=2*h*(l+b)
        print("AI Result:The lateral surface area of the cuboid is: ",lateral_surface_area)
    elif "area of base" in command or'base area'in command:
        a_b=l*b
        print("AI Result:The area of base of cuboid is: ",a_b)
    elif "face diogonal" in command or "fd" in command:
        f_d=square_root*(l**2+b**2)
        print("AI Result:face diogonal of the cuboid is: ",f_d)
    elif "body diogonal"in command or "bd" in command:
        b_d=square_root*(l**2+b**2+h**2)
        print("AI result:The body diagonal of the cuboid is: ",b_d)
    elif "volume"in command or "v" in command:
        v=l*b*h
        print("AI Result:volume of the cuboid is: ",v)
    else:
        print("AI Error:Sorry,I am only trained to calculate the cuboid's properties  like total edge length,area of one face,perimeter of one face,total surface area,lateral surface area,volume,length of body digonal and face")
        input('Please press Enter button to exit')
elif shape_choice=="cylinder":
    print("AI:You entered cylinder.")
    while True:
        try:
            h=float(input("Enter the height of the cylinder: "))
            r=float(input("Enter the radius of the cylinder: "))
            if h<=0 or r<=0:
                print("AI Error:The radius or height of any 3D shapes can never be less than or equal to zero.Please enter the appropriate positive value.")
            else:
                break
        except ValueError:
            print ("AI Error:You entered the digit in letters.Please type a number(like 5),not words!")
    if "circumference of circular base"in command or "c" in  command:
        c=2*PI*r
        print("The circumference of the circular base of thr cylinder is: ",c)
    elif "area of circular base"in command or "a" in command:
        a=PI*(r**2)
        print("AI Result:The area of circular base of the cylinder is: ",a)
    elif "curved surface area"in command or "lateral surface area"in command or "csa"in command or "lsa" in command:
        c_s_a=2*PI*r*h
        print("AI Result:The curved or lateral surface area of the cylinder is: ",c_s_a)
    elif "total surface area"in command or "tsa" in command:
        t_s_a=2*PI*r*(r+h)
        print("AI Result:The total surface area of the cylinder is: ",t_s_a)
    elif "volume"in command or "v" in command:
        v=PI*(r**2)*h
        print("AI Result:The volume of the cylinder is: ",v)
    elif 'diameter'in command or 'd' in command:
        d=2*r
        ("AI Result:The diameter of the cylinder is: ",d)
    else:
        print("AI Error:I am only trained to calculate the cylinder's properties like diameter,circumference of the circular base,area of the the circular base,curved or lateral surface area,total surface area,volume of the cylinder")
        input('Please press Enter button to exit')
elif shape_choice=='frustum':
    while True:
        try:
            R=float(input("Enter the larger radius(bottom) of the frustum: "))
            r=float(input("Enter the smaller radius(top) of the frustum: "))
            h=float(input('Enter the hight of the frustum: '))
            if R<=0 or r<=0 or h<=0 :
                          print('AI Error:The smaller or larger radius,height or of any 3D shapes can never be less than or equal to zero.please enter the appropriate positive value.')
            else:
                break
        except ValueError:
            print('AI Error:You entered the value of digit in letters.Please type a number(like5),not words!')
    if "larger diameter" in command or "D" in command:
        D=2*R
        print("AI Result:The larger diameter of the frustum is: ",D)
    elif "smaller diameter"in command or 'd' in command:
        d=2*r
        print("AI Result:The smaller diameter of the frustum is: ",d)
    elif 'slant height'in command or 'sl' in command:
        l=square_root((h**2)+((R-r)**2))
        print("AI Result:The slant height of the frustum is: ",l)
    elif 'difference between radius'in command or 'diff btw radii' in command:
        Diff=R-r
        print("AI Result:The difference between the larger and smaller radius is: ",Diff)
    elif 'curved surface area'in command or 'lateral surface area'in command or 'lsa'in command or 'csa' in command:
        c_s_a=PI*(R+r)*l
        print("AI Result:The curved or lateral surface area of the frustum is: ",c_s_a)
    elif 'total surface area'in command or 'lsa' in command:
        t_s_a=PI*(R+r)*l+PI*(R**2)+PI*(r**2)
    elif 'volume'in command or 'v' in command:
        v=(1/3)*PI*h*((R**2)+(r**2)+(R*r))
        print("AI Result:The volume of the frustum is: ",v)
    else:("AI Error:Sorry,I am only trained to calculate the frustum's properties like total surface area,curved or lateral surface area,larger and smaller diameter,volume and slant height.")
    input('Please press Enter button to exit')
elif shape_choice=="cone":
    print("AI:You entered cone!")
    while True:
        try:
            r=float(input("Enter the radius of base of the cone: "))
            h=float(input("Enter the perpendicular height of the cone: "))
            if r<=0 or h<=0:
                    print("AI Error:The radius and height of any 3D shapes can never be less than or equal to zero!.Please enter appropriate positive value.")
            else:
                break
        except ValueError:
            print("AI Error:You entered the value of digit in letters.Please type a number(like5),not words!")
    if "diameter of base" in command or 'd' in command:
        d=2*r
        print("AI Result:The diameter of the base of the cone is: ",d)
    elif "slant height" in command or 'sh' in command:
        s_l=square_root((r**2)+(h**2))
        print("AI Result:The slant height of the cone is: ",s_l)
    elif " base area" in command:
        a= PI*(r**2)
        print("AI Result:The base area of the cone is: ",a)
    elif "curved surface area" in command or 'lateral surface area' in command or 'lsa' in command or 'tsa' in command:
        c_s_a=PI*r*(square_root((r**2)+(h**2)))
        print("AI Result:The curved or lateral surface area of the cone is: ",c_s_a)
    elif "total surface area" in command or 'tsa' in command:
        t_s_a=PI*r*(r+(sqrt((r**2)+(h**2))))
        print('AI Result:The total surface area of the cone is: ',t_s_a)
    elif 'volume' in command or 'v' in command:
        v=(1/3)*PI*(r**2)*h
        print('AI Result:The volume of the cone is: ',v)
    elif'circumference of base of cone' in command:
        c=2*PI*r
        print("AI Error:The circumference of the base of cone is: ",c)
    else:
        print("AI Error:Sorry,I am only trained to calculate the cone's properties like diameter of base,slant height,area of base,total surface area,curved or lateral surface area and volume of the cone")
elif shape_choice=="hemisphere":
    print("AI:You entered hemisphere!")
    while True:
        try:
            r=float(input("enter the radius of the hemisphere: "))
            if r<=0:
                print('AI Error:The radius of any 3D shapes can never be less than or equal to zero!.Please enter approprite positive value.')
            else:
                break
        except ValueError:
            print("AI Error:You entered the value of digit in letters.Please type a number(like5),not words!")
    if 'diameter' in command or 'd' in command:
        d=2*r
        print("AI Result:The diameter of the hemisphere is: ",d)
    elif 'base area' in command or 'a'in command:
        b=PI*(r**2)
        print('AI Result:The base area of the hemisphere is: ',b)
    elif 'height' in command:
        h=r
        print('AI Result:The height of the hemisphere is: ',h)
    elif 'curved surface area'in command or 'lateral surface area' in command or 'csa' in command or 'lsa' in command:
        c=2*PI*(r**2)
        print('AI Result:The curved or lateral surfae area of the hemisphere is: ',c)
    elif'total surface area' in command or 'tsa' in command:
        t=3*PI*(r**2)
        print('AI Result:The total surface area of the hemisphere is: ',t)
    elif'circumference of the base' in command:
        c=2*PI*r
        print('AI Result:The circumference of the base of the hemisphere is: ',c)
    elif'volume' in command or'v' in command:
        v=(2/3)*PI*(r**3)
        print('AI Result:The volume of the hemisphere is: ',v)
    else:
        print("AI Error:Sorry,I am only trained to calculte the hemisphere's properties like diameter,circumference and area of the base,curved or lateral surface area,total surface area and volume.")
    input('Please press Enter button to exit')
elif shape_choice=='sphere':
    print('You entered sphere!.')
    while True:
        try:
            r=float(input('Enter the radius of the sphere: '))
            if r<=0:
               print('AI Error:The radius of any 3D shapes cab never be less than or equal to zero!.Please enter appropriate postive value.')
            else:
                break
        except ValueError:
            print('AI Error:You entered the value of digit in letters.Please type a number(like5),not words!')
    if "volume" in command or 'v'in command:
        v=(4/3)*PI*(r**3)
        print("AI Result: The volume of the sphere is: ",v)
    elif "circumference" in command or 'c' in command:
        c=2*PI*r
        print("AI Result: The circumference of the sphere is: ",c)
    elif " total surface area" in command or 'tsa' in command:
        t_s_a=4*PI*(r**2)
        print('AI Result: The total surface  area of the sphere is: ',t_s_a)
    elif " area" in command or'a' in command:
        a=PI*(r**2)
        print("AI Result: The  area of the sphere is: ",a)
    elif 'diameter' in command or 'd' in command:
        d=2*r
        print('AI Result:The diameter of the sphere is: ',d)
    else:
        print("AI Result:Sorry,I am only trained to calculate the sphere's properties like circumference,area,total surface area,diameter and volume.")  
    input('Please press Enter button to exit')