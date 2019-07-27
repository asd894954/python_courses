Сеттеры и геттеры

1) раньше все было просто у класса были переменные

![alt text](image/image1.png "xzxz")

 
2) потом подумали что если изменяется некоторая переменная класса, то может изменится и другая.  Например если в машине количество мест превышает 6, то это не частная машина, а общественный транспорт, и чтобы минимизировать количество написанного кода сложили это все в класс и назвали  сеттеры и геттеры

 ![alt text](image/image2.png "xzxz")

3) потом подумали что каждый раз писать

 ![alt text](image/image3.png "xzxz")

вместо

 ![alt text](image/image4.png "xzxz")



как-то напряжно и придумали properties

 ![alt text](image/image5.png "xzxz")

теперь можно писать так

 ![alt text](image/image6.png "xzxz")

4) вот они все напридумывали, а нам теперь на каждую переменную  писать лишних 8 строк осмысленного кода.  Дабы сократить бессмысленный вод текста придумали code snippet

идем в file → settings →live templates

 ![alt text](image/image7.png "xzxz")

в ветке Python создаем

 ![alt text](image/image8.png "xzxz")

заполняем

 ![alt text](image/image9.png "xzxz")

и в поле ввода пишем это


>_$var_name$ = None
>
>def set_$var_name$(self,$var_name$):
>    self._$var_name$ = $var_name$
>
>def get_$var_name$(self):
>    return self._$var_name$
>
>def del_$var_name$(self):
>    del self._$var_name$
>
>$var_name$ = property(get_$var_name$, set_$var_name$, del_$var_name$, "I'm the '$var_name$' property.")

 ![alt text](image/image10.png "xzxz")

указываем где наш сниппет может вызываться

 ![alt text](image/image11.png "xzxz")


в итоге мы можем делать следующее

 ![alt text](image/image12.gif "xzxz")

в итоге вернулись к началу, просто внутри  может происходить что-то особенное.  В 99% случаев там не будет ничего особенного кроме присвоения переменных,  [просто здесь так принято](https://onedio.ru/news/zanimatelnaya-sociologiya-5-obezyan-lestnicy-i-banany-12717) и в вас будут тыкать пальцами если вы будете делать по другому.
