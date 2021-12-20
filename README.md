# Web_server
## Дополнительные задания
1. При ответе вашего сервера посылайте некоторые основные заголовки:  
Date  
Content-type  
Server  
Content-length  
Connection: close.  
![image](https://user-images.githubusercontent.com/70998859/146726621-d72161a1-d319-4ba2-9679-7d37be3fc34c.png)   
2. Создайте файл настроек вашего веб-сервера, в котором можно задать прослушиваемый порт, рабочую директорию, максимальный объем запроса в байтах. Можете добавить собственные настройки по желанию.  
![image](https://user-images.githubusercontent.com/70998859/146726814-547408a0-59bd-449c-b5e1-0a8584c8e666.png)  
3. Если файл не найден, сервер передает в сокет специальный код ошибки - 404.  
![image](https://user-images.githubusercontent.com/70998859/146726848-519ae21b-5e00-4b5c-8fd4-d86f5ca3f051.png)  
4. Сервер должен работать в многопоточном режиме.  
![image](https://user-images.githubusercontent.com/70998859/146726908-95e34328-ff50-4a39-b0b4-feb03747cfbe.png)  
5. Сервер должен вести логи в следующем формате: Дата запроса. IP-адрес клиента, имя запрошенного файла, код ошибки.  
![image](https://user-images.githubusercontent.com/70998859/146726950-18e58b71-875c-4690-b74e-ba8dd8689a04.png)  
6. Добавьте возможность запрашивать только определенные типы файлов (.html, .css, .js и так далее). При запросе неразрешенного типа, верните ошибку 403.  
![image](https://user-images.githubusercontent.com/70998859/146727115-55420437-542a-4855-a285-d004ad0f850b.png)  
![image](https://user-images.githubusercontent.com/70998859/146727145-9b5a6ef2-5d28-4f7d-b0a5-364e26a9cc87.png)  
7. Реализуйте поддержку постоянного соединения с несколькими запросами.  
![image](https://user-images.githubusercontent.com/70998859/146727334-a3209828-4e94-422e-a1d5-5301a284590a.png)  
8. Реализуйте поддержку бинарных типов данных, в частночти, картинок.  
![image](https://user-images.githubusercontent.com/70998859/146727375-e21fe0d8-88d4-4f59-8051-b4bff42e2de6.png)  
