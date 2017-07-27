<?php
	/**
	 * 返回查询到的所有物品
	 */
	error_reporting(E_ALL || ~E_NOTICE);
	header("Content-Type: text/html; charset=utf-8");
	$con = mysql_connect("localhost","root","");
	if (!$con)
		die('contect mysql fail:' . mysql_error());
	mysql_select_db("", $con);
	mysql_query("set names utf8");
	
	$result = mysql_query("SELECT * FROM commodity");

	while($row = mysql_fetch_assoc($result)){
		$name[] = $row['name'];
		$price[] = $row['price'];
	}
	
	echo json_encode(array('name'=>$name, 'price'=>$price));
?>