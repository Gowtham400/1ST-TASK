{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3be44edb",
   "metadata": {},
   "source": [
    "# VARIABLES"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "681d1170",
   "metadata": {},
   "outputs": [],
   "source": [
    "#declaring variables\n",
    "var1 = 7\n",
    "var2 = 18\n",
    "\n",
    "#swapping variables\n",
    "var1,var2 = var2,var1\n",
    "\n",
    "print(\"var1 = \",var1)\n",
    "print(\"var2 = \",var2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "83744662",
   "metadata": {},
   "source": [
    "# NUMBERS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7666f64d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "var1 =  18\n",
      "var2 =  7\n"
     ]
    }
   ],
   "source": [
    "x=2\n",
    "y=1.2\n",
    "print(\"int(x)= \",int(x))\n",
    "print(\"int(y)= \",int(y))\n",
    "print(\"float(y)= \",float(y))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c4b099b",
   "metadata": {},
   "source": [
    "# STRING"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f6e56edc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "m\n",
      "wtham\n",
      "Gowtham\n",
      "5\n",
      "mahtwog\n"
     ]
    }
   ],
   "source": [
    "s = \"gowtham\"\n",
    "#last character\n",
    "print(s[-1])\n",
    "#slicing first two characters\n",
    "print(s[2:])\n",
    "#converting first character to upper case\n",
    "print(s.capitalize())\n",
    "#finding the character in string\n",
    "print(s.index(\"a\"))\n",
    "#reversing\n",
    "s = s[::-1]\n",
    "print(s)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f93826b0",
   "metadata": {},
   "source": [
    "# List"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c570269c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5, 9, 'cool', 6, 'sunny', 2, '21']\n",
      "cool\n",
      "[17, 43, 22, 63, 48, 21]\n",
      "[17, 21, 22, 43, 48, 63]\n"
     ]
    }
   ],
   "source": [
    "list1 = [5,9,\"cool\",6,\"sunny\",2]\n",
    "list2 = [21,48,63,22,43,17]\n",
    "#adding string to the list at end\n",
    "list1.append(\"21\")\n",
    "print(list1)\n",
    "#popping the element\n",
    "print(list1.pop(2))\n",
    "#reversing\n",
    "list2.reverse()\n",
    "print(list2)\n",
    "#sorting the elements in the list\n",
    "list2.sort()\n",
    "print(list2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76684307",
   "metadata": {},
   "source": [
    "# Dictionary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "02426198",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n",
      "dict_items([('name', 'lucky'), ('age', '25'), ('experience', '2 years'), ('company', 'cureya')])\n",
      "cureya\n"
     ]
    }
   ],
   "source": [
    "employee ={\n",
    "    \"name\" : \"lucky\",\n",
    "    \"age\" : \"25\",\n",
    "    \"experience\":\"2 years\",\n",
    "    \"company\" : \"cureya\"\n",
    "}\n",
    "#getting specified value\n",
    "print(employee.get(\"age\"))\n",
    "\n",
    "#all items in the dictionary\n",
    "print(employee.items())\n",
    "\n",
    "#popping the specified element\n",
    "print(employee.pop(\"company\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27e190da",
   "metadata": {},
   "source": [
    "# Tuples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "d177d57d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3, 'thursday', 'friday', 2, 3)\n",
      "(2, 3, 'thursday')\n",
      "7\n",
      "<class 'tuple'>\n",
      "2\n",
      "(1, 2, 3, 'thursday', 'friday', 2, 3)\n"
     ]
    }
   ],
   "source": [
    "tup1 = 1,2,3\n",
    "tup2 = ('thursday','friday',2,3)\n",
    "#adding tuples\n",
    "tup3 = (tup1 + tup2)\n",
    "print(tup3)\n",
    "#slicing\n",
    "print(tup3[1:4])\n",
    "#length of tuple\n",
    "print(len(tup3))\n",
    "#to find if a tuple or not\n",
    "print(type(tup3))\n",
    "#no.of times item occurs\n",
    "print(tup3.count(3))\n",
    "#deleting the tuple\n",
    "del tup2\n",
    "#now for printing tup3 tup2 need not to be defined\n",
    "print(tup3)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b129a3c5",
   "metadata": {},
   "source": [
    "# if-statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "91a5cb6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a= 81 ,b= 0\n",
      "enter sum a+b: 70\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "num1 = random.randint(0,99)\n",
    "num2 = random.randint(0,99)\n",
    "\n",
    "print('a=',num1 ,',' 'b=',num2)\n",
    "#user expects the sum of random numbers\n",
    "sum = eval(input(\"enter sum a+b: \"))\n",
    "result = num1 + num2\n",
    "#if statement to state whether the user is right or wrong\n",
    "if sum is result:\n",
    "    print(\"TRUE\")\n",
    "else:\n",
    "    print(\"False\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4048293",
   "metadata": {},
   "source": [
    "# For-loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "35069b0c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " The perfect numbers below 10000 are : \n",
      "6\n",
      "28\n",
      "496\n",
      "8128\n"
     ]
    }
   ],
   "source": [
    "#a perfect number is the sum of its positive divisors\n",
    "print(\" The perfect numbers below 10000 are : \")\n",
    "for i in range (1,10000):\n",
    "    x=0\n",
    "    for j in range (1,i):\n",
    "        if i%j==0:\n",
    "            x=x+j\n",
    "    if x==i:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c2b77e8",
   "metadata": {},
   "source": [
    "# Arithmetic"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "69fc3106",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "area of rectangle1 is  36.9\n",
      "perimeter of rectangle1 is  26.2\n",
      "area of rectangle2 is  16.5\n",
      "perimeter of rectangle2 is  17.0\n",
      "rectangle1 is  2 times bigger than rectangle2\n"
     ]
    }
   ],
   "source": [
    "#dimensions of rectangle1\n",
    "w1 = 4.1\n",
    "l1 = 9\n",
    "#dimensions of rectangle2\n",
    "w2 = 3\n",
    "l2 = 5.5\n",
    "\n",
    "print(\"area of rectangle1 is \",w1*l1)\n",
    "print(\"perimeter of rectangle1 is \",2*(l1+w1))\n",
    "\n",
    "print(\"area of rectangle2 is \",l2*w2)\n",
    "print(\"perimeter of rectangle2 is \",2*(l2+w2))\n",
    "\n",
    "ratio = (w1*l1)/(w2*l2)\n",
    "#to avoid decimal in ratio i'll convert it to integer\n",
    "print(\"rectangle1 is \",int(ratio),\"times bigger than rectangle2\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dbf7b5d",
   "metadata": {},
   "source": [
    "# Numpy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "85e2ec53",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(2, 3)\n",
      "[[5 6]\n",
      " [4 1]\n",
      " [2 3]]\n",
      "[6 3]\n",
      "[5 6 4]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "a=np.array([[5,6,4],[1,2,3]])\n",
    "print(np.shape(a))\n",
    "\n",
    "b=np.reshape(a,(3,2))\n",
    "print(b)\n",
    "\n",
    "\n",
    "#maximum value along row\n",
    "n=np.max(a,1)\n",
    "print(n)\n",
    "#max value along coloumn\n",
    "k=np.max(a,0)\n",
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "eb91e1d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 1.  3.  3.]\n",
      " [ 7. 89. 39.]]\n",
      "[[ 1.   3.2  3.4]\n",
      " [ 7.  88.8 38.7]\n",
      " [ 1.   2.   3. ]\n",
      " [45.   5.   6. ]]\n",
      "[[ 1.   3.2  3.4  1.   2.   3. ]\n",
      " [ 7.  88.8 38.7 45.   5.   6. ]]\n"
     ]
    }
   ],
   "source": [
    "p=np.array([[1,3.2,3.4],[7,88.8,38.7]])\n",
    "#rounding the elements to nearest integers\n",
    "print(np.round(p))\n",
    "\n",
    "q=np.array([[1,2,3],[45,5,6]])\n",
    "#joining the two arrays along column\n",
    "print(np.concatenate((p,q),axis=0))\n",
    "\n",
    "#joining the two arrays along row\n",
    "print(np.concatenate((p,q),axis=1))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "95a7f850",
   "metadata": {},
   "source": [
    "# Matplotlib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "372c97cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "a=np.array([1,2,3,4,5,6,7,8])\n",
    "\n",
    "#declaring the equation\n",
    "b=a**2+a*2+1\n",
    "\n",
    "#defining the graph along both axis\n",
    "plt.xlabel('x-axis')\n",
    "plt.ylabel('y-axis')\n",
    "\n",
    "#naming the plot\n",
    "plt.title('graph')\n",
    "\n",
    "#assigning x,y axis values\n",
    "plt.plot(b,a)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b461b81e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "from matplotlib import pyplot as plt\n",
    "\n",
    "\n",
    "no_of_mobiles=[1,3,4,7,5,10]\n",
    "day=[1,2,3,4,5,6]\n",
    "\n",
    "#assigning x,y axis values to bar graph\n",
    "plt.bar(day,no_of_mobiles)\n",
    "#naming the graph\n",
    "plt.title('mobile sales')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3320cdb1",
   "metadata": {},
   "source": [
    "# Pandas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f47bd92b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    mobile  ratings       sales\n",
      "0    apple      5.0   207847528\n",
      "1   realme      4.5  1303171035\n",
      "2  Oneplus      4.8    11190846\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "#assigning dataset\n",
    "data = {'mobile': ['apple',  'realme',  'Oneplus'],\n",
    "\n",
    "        \n",
    "'ratings': [5,4.5,4.8],\n",
    "\n",
    "'sales': [207847528, 1303171035, 11190846]}\n",
    "\n",
    "#setting the dataframe\n",
    "df= pd.DataFrame(data,columns=['mobile',  'ratings',  'sales'])\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a0a394b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
