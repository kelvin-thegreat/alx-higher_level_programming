-- Lists all genres of show Dexter in the DB hbtn_0d_tvshows.
-- order by ascending genre name.
SELECT tvg.`name`
  FROM `tv_genres` AS tvg
       INNER JOIN `tv_show_genres` AS s
       ON tvg.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS tvs
       ON tvs.`id` = s.`show_id`
       WHERE tvs.`title` = "Dexter"
 ORDER BY tvg.`name`;
