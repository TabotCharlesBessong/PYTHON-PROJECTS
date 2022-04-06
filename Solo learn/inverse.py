# also work without input 

# If you don't 'know what is matrix then just click on submit  button without entering any input to view random result.

# if you know matrix then here you can find inverse of any 3×3 matrix.

# Note: while entering input add row wise elements of matrix and each new element start from new line and add only 9 elements because 3×3 matrix contains only 9 elements, example input:

#1

#2

#4

#5

#6

#7

#3

#45

#-10

import os

from timeit import default_timer as timer

from fractions import Fraction as frac

import random 

initial_time = timer()

try:

    a11 = int(input())

    a12 = int(input())

    a13 = int(input())

    a21 = int(input())

    a22 = int(input())

    a23 = int(input())

    a31 = int(input())

    a32 = int(input())

    a33 = int(input())

except:

    a11 = round(random.randint(-10,10))

    a12 = round(random.randint(-10,10))

    a13 = round(random.randint(-10,10))

    a21 = round(random.randint(-10,10))

    a22 = round(random.randint(-10,10))

    a23 = round(random.randint(-10,10))

    a31 = round(random.randint(-10,10))

    a32 = round(random.randint(-10,10))

    a33 = round(random.randint(-10,10))

A11 = (a22*a33)-(a23*a32)

A12 = -((a21*a33)-(a23*a31))

A13 = (a21*a32)-(a22*a31)

A21 = -((a12*a33)-(a13*a32))

A22 = (a11*a33)-(a13*a31)

A23 = -((a11*a32)-(a12*a31))

A31 = (a12*a23)-(a13*a22)

A32 = -((a11*a23)-(a13*a21))

A33 = (a11*a22)-(a12*a21)

Determinant = a11*int(A11) + a12*int(A12) + a13*int(A13)

print ("""<h2 align="center" style="color:#boddf2; padding:10px; border:5px solid transparent; border-image: linear-gradient(to right, #FDEB71, #EA5455, #7367F0, #9F44D3, #F55555); border-image-slice: 1; border-color: #83eeff; box-shadow: 0 0 10px #83eeff; text-color: #83eeff; text-shadow: 0 0 10px #83eeff;">Matrix Inverse Calculator<br>(3×3)</h2>""")

print (f"""<h3 style="color:#3fff00;">Let given matrix is :</h3><table>

<tr>

<td>A = </td>

<td>[</td>

<td style="text-align: center;">{a11}</td>

<td style="text-align: center;">{a12}</td>

<td style="text-align: center;">{a13}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{a21}</td>

<td style="text-align: center;">{a22}</td>

<td style="text-align: center;">{a23}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{a31}</td>

<td style="text-align: center;">{a32}</td>

<td style="text-align: center;">{a33}</td>

<td>]</td>

</tr>

</table>

<h3 style="color:#3fff00;">Determinant of matrix :</h3>|A| =  {a11}[({a22})×({a33}) - ({a23})×({a32})] - ({a12})[({a21})×({a33})-({a23})×({a31})] + ({a13})[({a21})×({a32})-({a22})×({a31})]

∴ |A| = {a11}[({a22*a33}) - ({a23*a32})] - ({a12})[({a21*a33})-({a23*a31})] + ({a13})[({a21*a32})-({a22*a31})]

∴ |A| = {a11}({a22*a33 - a23*a32}) - ({a12})({a21*a33-a23*a31}) + ({a13})({a21*a32-a22*a31})

∴ |A| = ({a11*(a22*a33 - a23*a32)}) - ({a12*(a21*a33-a23*a31)}) + ({a13*(a21*a32-a22*a31)})

∴ |A| =  {Determinant}

""")

os.system("touch file.png")

if Determinant == 0 :

   print ("∵ Determinant i.e. |A| = 0, so this is singular matrix, \n Hence this matrix is not invertible \n∴ A\u207B¹ not exsits.")

   

else :

    i11=frac(A11, Determinant)

    i12=frac(A21, Determinant)

    i13=frac(A31, Determinant)

    i21=frac(A12, Determinant)

    i22=frac(A22, Determinant)

    i23=frac(A32, Determinant)

    i31=frac(A13, Determinant)

    i32=frac(A23, Determinant)

    i33=frac(A33, Determinant)

    r11=round(A11 / Determinant,4)

    r12=round(A21 / Determinant,4)

    r13=round(A31 / Determinant,4)

    r21=round(A12 / Determinant,4)

    r22=round(A22 / Determinant,4)

    r23=round(A32 / Determinant,4)

    r31=round(A13 / Determinant,4)

    r32=round(A23 / Determinant,4)

    r33=round(A33 / Determinant,4)

    

    print (f"""∴ |A| = {Determinant} ≠ 0  (Matrix is Invertible)

∴ A\u207B¹ exsits.

<h3 style="color:#3fff00">Co-factor elements :</h3><table>

<tr>

<td>A₁₁</td>

<td>=</td>

<td>(-1)¹⁺¹M₁₁ =   1 ×</td>

<td>|</td>

<td style="text-align: center;">{a22}</td>

<td style="text-align: center;">{a23}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A11}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a32}</td>

<td style="text-align: center;">{a33}</td>

<td>|</td>

</tr>

<tr>

<td>A₁₂</td>

<td>=</td>

<td>(-1)¹⁺²M₁₂ = -1 ×</td>

<td>|</td>

<td style="text-align: center;">{a21}</td>

<td style="text-align: center;">{a23}</td>

<td>|</td>

<td>=</td>

<td style="text-align: center;">{A12}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a31}</td>

<td style="text-align: center;">{a33}</td>

<td>|</td>

</tr>

<tr>

<td>A₁₃</td>

<td>=</td>

<td>(-1)¹⁺³M₁₃ =   1 ×</td>

<td>|</td>

<td style="text-align: center;">{a21}</td>

<td style="text-align: center;">{a22}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A13}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a31}</td>

<td style="text-align: center;">{a32}</td>

<td>|</td>

</tr>

<tr>

<td>A₂₁</td>

<td>=</td>

<td>(-1)²⁺¹M₂₁ = -1 ×</td>

<td>|</td>

<td style="text-align: center;">{a12}</td>

<td style="text-align: center;">{a13}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A21}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a32}</td>

<td style="text-align: center;">{a33}</td>

<td>|</td>

</tr>

<tr>

<td>A₂₂</td>

<td>=</td>

<td>(-1)²⁺²M₂₂ =   1 ×</td>

<td>|</td>

<td style="text-align: center;">{a11}</td>

<td style="text-align: center;">{a13}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A22}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a31}</td>

<td style="text-align: center;">{a33}</td>

<td>|</td>

</tr>

<tr>

<td>A₂₃</td>

<td>=</td>

<td>(-1)²⁺³M₂₃ = -1 ×</td>

<td>|</td>

<td style="text-align: center;">{a11}</td>

<td style="text-align: center;">{a12}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A23}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a31}</td>

<td style="text-align: center;">{a32}</td>

<td>|</td>

</tr>

<tr>

<td>A₃₁</td>

<td>=</td>

<td>(-1)³⁺¹M₃₁ =   1 ×</td>

<td>|</td>

<td style="text-align: center;">{a12}</td>

<td style="text-align: center;">{a13}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A31}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a22}</td>

<td style="text-align: center;">{a23}</td>

<td>|</td>

</tr>

<tr>

<td>A₃₂</td>

<td>=</td>

<td>(-1)³⁺²M₃₂ = -1 ×</td>

<td>|</td>

<td style="text-align: center;">{a11}</td>

<td style="text-align: center;">{a13}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A32}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a21}</td>

<td style="text-align: center;">{a23}</td>

<td>|</td>

</tr>

<tr>

<td>A₃₃</td>

<td>=</td>

<td>(-1)³⁺³M₃₃ =   1 ×</td>

<td>|</td>

<td style="text-align: center;">{a11}</td>

<td style="text-align: center;">{a12}</td>

<td style="text-align: center;">|</td>

<td>=</td>

<td style="text-align: center;">{A33}</td>

</tr>

<td></td>

<td></td>

<td></td>

<td>|</td>

<td style="text-align: center;">{a21}</td>

<td style="text-align: center;">{a22}</td>

<td>|</td>

</tr>

</table>

<h3 style="color:#3fff00;">∴ The matrix of Co-factor elements is :</h3><table>

<tr>

<td>   [Aᵢⱼ]₃ₓ₃ = </td>

<td>[</td>

<td style="text-align: center;">A₁₁</td>

<td style="text-align: center;">A₁₂</td>

<td style="text-align: center;">A₁₃</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">A₂₁</td>

<td style="text-align: center;">A₂₂</td>

<td style="text-align: center;">A₂₃</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">A₃₁</td>

<td style="text-align: center;">A₃₂</td>

<td style="text-align: center;">A₃₃</td>

<td>]</td>

</tr>

</table>

<table>

<tr>

<td>∴ [Aᵢⱼ]₃ₓ₃ = </td>

<td>[</td>

<td style="text-align: center;">{A11}</td>

<td style="text-align: center;">{A12}</td>

<td style="text-align: center;">{A13}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{A21}</td>

<td style="text-align: center;">{A22}</td>

<td style="text-align: center;">{A23}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{A31}</td>

<td style="text-align: center;">{A32}</td>

<td style="text-align: center;">{A33}</td>

<td>]</td>

</tr>

</table>

<h3 style="color:#3fff00;">∴ Adjoint matrix is :</h3><p>    adj(A) = ([Aᵢⱼ]₃ₓ₃)ᵀ</p><table>

<tr>

<td>∴ adj(A) = </td>

<td>[</td>

<td style="text-align: center;">{A11}</td>

<td style="text-align: center;">{A21}</td>

<td style="text-align: center;">{A31}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{A12}</td>

<td style="text-align: center;">{A22}</td>

<td style="text-align: center;">{A32}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{A13}</td>

<td style="text-align: center;">{A23}</td>

<td style="text-align: center;">{A33}</td>

<td>]</td>

</tr>

</table>

<h3 style="color:#3fff00;">∴ Inverse of matrix is :</h3><table>

<tr>

<td>   A\u207B¹ =</td>

<td> 1/|A| × adj(A)</td>

</tr></table>

<table>

<tr>

<td>∴ A\u207B¹ =</td>

<td>1/{Determinant} × </td>

<td>[</td>

<td style="text-align: center;">{A11}</td>

<td style="text-align: center;">{A21}</td>

<td style="text-align: center;">{A31}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td></td>

<td>[</td>

<td style="text-align: center;">{A12}</td>

<td style="text-align: center;">{A22}</td>

<td style="text-align: center;">{A32}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td></td>

<td>[</td>

<td style="text-align: center;">{A13}</td>

<td style="text-align: center;">{A23}</td>

<td style="text-align: center;">{A33}</td>

<td>]</td>

</tr>

</table>

<table>

<tr>

<td>∴ A\u207B¹ =</td>

<td>[</td>

<td style="text-align: center;">{i11}</td>

<td style="text-align: center;">{i12}</td>

<td style="text-align: center;">{i13}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{i21}</td>

<td style="text-align: center;">{i22}</td>

<td style="text-align: center;">{i23}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{i31}</td>

<td style="text-align: center;">{i32}</td>

<td style="text-align: center;">{i33}</td>

<td>]</td>

</tr>

</table><h3 style="color:#FFD700">(or)</h3><table>

<tr>

<td>∴ A\u207B¹ ≈</td>

<td>[</td>

<td style="text-align: center;">{r11}</td>

<td style="text-align: center;">{r12}</td>

<td style="text-align: center;">{r13}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{r21}</td>

<td style="text-align: center;">{r22}</td>

<td style="text-align: center;">{r23}</td>

<td>]</td>

</tr>

<tr>

<td></td>

<td>[</td>

<td style="text-align: center;">{r31}</td>

<td style="text-align: center;">{r32}</td>

<td style="text-align: center;">{r33}</td>

<td>]</td>

</tr>

</table>""")

print ("""

<hr style="border: 3px dashed #FF1493;">

<h2 align="center"><a href="https://www.sololearn.com/profile/23363542" target="_blank" class="Sololearn_Profile" style="text-decoration:none; color:#FF7722;">Made with ❤️ by @sujal</a></h2><h3 align="center" style="color:#e8ffc6">Give "👍" and "💬" if you like this code or find it helpful</h3><h4 align="center" style="color:#00ff7f">If you found any error or have any suggestion please write in comment</h4>""")

final_time = timer()

print(f"""<p align="center" style="color:#00FFFF;">Execution time of the program : 

{final_time - initial_time}</p>

<hr style="border: 3px dashed #FF1493;">""")

os.system("touch file.png")
