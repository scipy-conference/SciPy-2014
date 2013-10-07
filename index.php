<?php

session_start();

?>


<!DOCTYPE html>
<html>
<?php $thisPage="Home"; ?>
<head>

<?php include('inc/header.php') ?>

<link rel="shortcut icon" href="http://conference.scipy.org/scipy2013/favicon.ico" />

</head>

<body>

<div id="container">

<?php include('inc/page_headers.php') ?>

<section id="slim_sidebar">
  <?php include("inc/sponsors_small.php") ?>
</section>

<section id="hp-content">

<div class="row">
  <div class="hp_cell">
    <h2>Attend</h2>
      <img src="img/about.png" width="251" height="84" alt="about scipy" class="hp_image" />
    <p>The annual SciPy Conference allows participants from academic, commercial, and governmental organizations to showcase their latest Scientific Python projects, learn from skilled users and developers, and collaborate on code development.</p>

    <p>We look forward to a very exciting conference and hope to see you at the 2014 conference.</p>
  </div>
  <div class="hp_cell" style="margin: 0 2%;">
    <h2>Schedule</h2>
        <p>The 2014 conference will consist of two days of tutorials followed by <strong>three days of presentations</strong>, and concludes with two days of developer sprints on projects of interest to the attendees.</p>
        <?php echo $display_dates ?>
        <div class="row" style="margin: 0;">
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Sunday</p>
            <p class="icon_date_day">6</p></div>
          </div>
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Monday</p>
            <p class="icon_date_day">7</p></div>
          </div>
          <div class="free_cell" style="max-width: 20%; padding-top: 1em;">
            Tutorials
          </div>
        </div>
        <div class="row" style="margin: 0;">
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Tuesday</p>
            <p class="icon_date_day">8</p></div>
          </div>
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Thursday</p>
            <p class="icon_date_day">10</p></div>
          </div>
          <div class="free_cell" style="max-width: 50%; padding-top: 1em;">
            Main Conference Session
          </div>
        </div>
        <div class="row" style="margin: 0;">
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Friday</p>
            <p class="icon_date_day">11</p></div>
          </div>
          <div class="free_cell">
            <div class="icon_date"><p>Jul</p>
            <p class="icon_date_w">Saturday</p>
            <p class="icon_date_day">12</p></div>
          </div>
          <div class="free_cell" style="max-width: 20%; padding-top: 1em;">
            Sprints
          </div>
        </div>
  </div>
  <div class="hp_cell">
    <h2>What's it like?</h2>
    <p>Watch the video highlighting last years conference.</p>
    <a href="video_highlights.php"><img src="img/video_placeholder.png" width="260" height="146" alt="SciPy 2013 video highlights" class="hp_image" /></a>
    <p style="font-size: 0.75em; color: #333; text-align: right; margin-right: 1em;"><em>Video courtesy of Enthought, Inc.</em></p>
  </div>
</div>



</section>



<div style="clear: both;"></div>
<footer id="page_footer">
<?php include('inc/page_footer.php') ?>
</footer>
</div>
</body>

</html>