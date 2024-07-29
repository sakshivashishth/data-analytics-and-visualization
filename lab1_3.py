
   
    "import numpy as np\n",
    "my_list=[1,2,3,4,5]\n",
    "arr=np.array(my_list)\n",
    "print(\"last index is:\",arr[-1])\n",
    "print(\"first index is:\",arr[0])\n",
    "print(\"multiply each element by 2\",arr*2)"
   
  

    "import numpy as np\n",
    "arr=np.zeros(10)\n",
    "print(\"an array of 10 zeroes: \\n\",arr)\n",
    "arr1=np.ones(10)\n",
    "print(\"an array of 10 ones: \\n\",arr1)\n",
    "arr2=np.ones(10)*5\n",
    "print(\"an array of 10 fives: \\n\",arr2)\n"
  
    "import numpy as np\n",
    "mat=np.random.randint(2,10,9).reshape(3,3)\n",
    "print(\"3*3 matrix is: \\n\",mat)"
 
    "import numpy as np                    #lab3\n",
    "category1=np.array([500,600,700,550])\n",
    "category2=np.array([450,700,800,600])\n",
    "total=category1+category2\n",
    "print(\"TOTAL REVENUE IS:\",total)"
  
    "import numpy as np\n",
    "revenue =np.array([10000,12000,11000,10500])\n",
    "expenses=np.array([4000,5000,4500,4800])\n",
    "profit=revenue-expenses\n",
    "print(\"profit\",profit)"
   
   
    "import numpy as np\n",
    "inventory=np.array([10,0,20,0,5,0])\n",
    "print(\"out of stock products:\",(inventory[inventory==0]))"
 
   
    "import numpy as np\n",
    "quantity=np.array([2,3,4,1])\n",
    "price_per_item=np.array([10.0,5.0,8.0,12.0])\n",
    "total=quantity*price_per_item\n",
    "print(\"total cost of items:\",total)"
  
  
