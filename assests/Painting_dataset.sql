 select * from artist; --421
 select * from canvas_size; --200
 select * from image_link; --14,775
 select * from museum_hours; -- 351
 select * from museum; -- 57
 select * from product_size; -- 110,347
 select * from subject; --6771
 select * from work; --14776

 Q10) Identify the museums which are open on both on both sunday and monday .Display museum name,city

 select * from museum_hours mh1
 where day = 'Monday'
 and exists (select 1 from museum_hours mh2
             where mh1.museum_hours = mh2.museum_ho
			 )