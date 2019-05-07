Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (1,"image 1 dun couple",'2008-01-01 10:00:00',2000,1500,7897,"/image/perso/couple/image1.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (2,"image 2 gars seul",'2029-08-09 15:14:20',300,300,8968,"/image/perso/solo/image2.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (3,"image 3 gars",'2018-01-01 20:20:33',2000,300,3213,"/image/perso/couple/image3.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (4,"image 4 paysage",'2023-05-03 13:00:00',2000,30000,24972,"/image/perso/paysage/image4.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (5,"image 5 stylo",'2007-01-01 10:00:00',424,242,2,"none");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (6,"image 6 deux couple",'2017-10-10 19:00:00',9242,2424,2,"/image/perso/obj/image6.JPG");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (7,"image 7 bille",'2007-01-01 10:00:00',5000,50021,89265,"/image/perso/obj/image7.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (8,"image 8 truc a la con",'2009-01-01 10:00:00',509,500,897,"/image/perso/couple/image8.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (9,"image 9 un gars",'2030-01-09 10:20:00',2000,2000,958738,"/image/perso/solo/image9.png");
Insert into IMAGE (id_image,comment,creation_date,length,width,size,path) values (10,"une couille",'2077-01-05 10:09:00',5000,5000,970,"/image/perso/couille/image10.png");

Insert into VECTOR (id_vector,value_vector,tag_name) values (1,"value vector1", "tag1");
Insert into VECTOR (id_vector,value_vector,tag_name) values (2,"value vector2", "tag2");
Insert into VECTOR (id_vector,value_vector,tag_name) values (3,"value vector3", "tag3");
Insert into VECTOR (id_vector,value_vector,tag_name) values (4,"value vector4", "tag4");
Insert into VECTOR (id_vector,value_vector,tag_name) values (5,"value vector5", "tag5");
Insert into VECTOR (id_vector,value_vector,tag_name) values (6,"value vector6", "tag6");
Insert into VECTOR (id_vector,value_vector,tag_name) values (7,"value vector7", "tag7");
Insert into VECTOR (id_vector,value_vector,tag_name) values (8,"value vector8", "tag8");
Insert into VECTOR (id_vector,value_vector,tag_name) values (9,"value vector9", "tag9");
Insert into VECTOR (id_vector,value_vector,tag_name) values (10,"value vector10", "tag10");

Insert into FACE_VECTOR (id_vector,IsKnown) values (1, 1);
Insert into FACE_VECTOR (id_vector,IsKnown) values (2, 1);
Insert into FACE_VECTOR (id_vector,IsKnown) values (3, 0);
Insert into FACE_VECTOR (id_vector,IsKnown) values (4, 0);
Insert into FACE_VECTOR (id_vector,IsKnown) values (6, 1);
Insert into FACE_VECTOR (id_vector,IsKnown) values (8, 0);
Insert into FACE_VECTOR (id_vector,IsKnown) values (9, 1);
Insert into FACE_VECTOR (id_vector,IsKnown) values (10, 0);

Insert into OBJECT_VECTOR(id_vector, id_parent) values(10,0);
Insert into OBJECT_VECTOR(id_vector, id_parent) values(7,0);
Insert into OBJECT_VECTOR(id_vector, id_parent) values(5,0);

Insert into INCLUDE(id_vector,id_image) values (1,1);
Insert into INCLUDE(id_vector,id_image) values (2,2);
Insert into INCLUDE(id_vector,id_image) values (3,3);
Insert into INCLUDE(id_vector,id_image) values (4,4);
Insert into INCLUDE(id_vector,id_image) values (5,5);
Insert into INCLUDE(id_vector,id_image) values (6,6);
Insert into INCLUDE(id_vector,id_image) values (7,7);
Insert into INCLUDE(id_vector,id_image) values (8,8);
Insert into INCLUDE(id_vector,id_image) values (9,9);
Insert into INCLUDE(id_vector,id_image) values (10,10);






