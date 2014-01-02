<?php
session_start();
?>
<!DOCTYPE html>
<html>
<?php $thisPage="Video Highlights"; ?>
<head>

<?php include('inc/header.php') ?>

<link rel="shortcut icon" href="http://conference.scipy.org/scipy2013/favicon.ico" />
</head>

<body>

<div id="container">

<?php include('inc/page_headers.php') ?>

<section id="sidebar">
  <?php include("inc/sponsors.php") ?>
</section>

<section id="main-content">

<h1>SciPy 2013 Video Highlights</h1>
<div style="display: block; width: 640px; margin: 0 auto;">
<iframe src="https://docs.google.com/a/enthought.com/file/d/0B0I7VMiDT-fTM2d0MFNFNVBIUzA/preview" width="640" height="385"></iframe>
</div>
</section>
<div style="clear:both;"></div>
<footer id="page_footer">
<?php include('inc/page_footer.php') ?>
</footer>
</div>
</body>

</html>