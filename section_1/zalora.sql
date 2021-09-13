1.
select 
	data.name as name,
	RANK () OVER ( ORDER BY sum(data.revenue) ) AS rank_number	
from (
select 
	s.faceid, 
	s.name,
	r.slots * s.guestcost  + r.slots * s.membercost as revenue
from 
zalora.public.stores s  
left join 
zalora.public.reservations r 
on
s.faceid = r.faceid ) as data
group by data.faceid, data.name
order by rank_number asc , data.name desc
limit 3


2. 
with revenue as (
select 
	data.faceid as faceid ,
	sum(data.revenue) as revenue
from (
select 
	s.faceid, 
	r.slots * s.guestcost  + r.slots * s.membercost as revenue
from 
zalora.public.stores s  
left join 
zalora.public.reservations r 
on
s.faceid = r.faceid ) as data
group by 1
)
select 
	s.faceid as faceid, 
	s."name" as storename,
	case
	when
		r.revenue < avarage_revenue then 'low'
	when 	
		r.revenue = avarage_revenue then 'avarage'
	when	
		r.revenue > avarage_revenue then 'high'		
	END as classification
from 
	revenue as r
left join
	zalora.public.stores s 	
on
 r.faceid = s.faceid 
left join
	(
		select 
			avg(r.revenue) as avarage_revenue 
		from 
		revenue r
	) as avg_r
on 
r.revenue = avg_r.avarage_revenue or r.revenue != avg_r.avarage_revenue
order BY 3, 2		


3. 
with august_2020_calendar as (
SELECT  
	CAST('2020-08-01' AS DATE) + (n || ' day')::interval as date_
FROM  
	generate_series(0, 30) n
), revenue as (
select 
	s.faceid,
	r.starttime, 
	r.slots * s.guestcost  + r.slots * s.membercost as revenue 
from 
	zalora.public.stores s  
left join 
	zalora.public.reservations r 
on
	s.faceid = r.faceid )

select 
 DATE(mc.date_) as date,
 ROUND(avg(r.revenue), 2) as revenue 
from 
 august_2020_calendar mc 
left join 
  revenue r 
on 
 EXTRACT(DAY FROM mc.date_ - DATE(r.starttime)) >= 0  and EXTRACT(DAY FROM mc.date_ - DATE(r.starttime)) <= 15 	
group by
 mc.date_	
order by 1 asc 
 


4. WITH RECURSIVE find_child AS (
   SELECT 15 AS id
   UNION ALL
   SELECT m.memid
   FROM zalora.public.members m 
      JOIN find_child ON find_child.id = m.recomended_by 
)
SELECT id FROM find_child;