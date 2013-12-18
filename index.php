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
    <a href="video_highlights.php"><img src="img/video_placeholder.png" width="100%" alt="SciPy 2013 video highlights" class="hp_image" /></a>
    <p style="font-size: 0.75em; color: #333; text-align: right; margin-right: 1em;"><em>Video courtesy of Enthought, Inc.</em></p>
  </div>
</div>

<div class="row">
  <div class="hp_cell">
    <h2>Stay Informed</h2>
    <p>To receive updates on conference specifics:</p>

  <img src="img/newsletter_icon.png" width="32" height="32"  alt="newsletter" class="callout_date" />
  <p>Subscribe to the SciPy 2014 announcements.</p>
  <style type="text/css">
.link,
.link a,
#SignUp .signupframe {
	color: #226699;
	font-family: Arial, Helvetica, sans-serif;
	font-size: 13px;
	border: none;
	}
	.link,
	.link a {
		text-decoration: none;
		}
	#SignUp .signupframe {
		width: 100%;
		border: 1px solid #000000;
		background: #ffffff;
		}
#SignUp .signupframe .required {
	font-size: 10px;
	}
</style>
<script type="text/javascript" src="http://app.icontact.com/icp/loadsignup.php/form.js?c=1254645&l=7470&f=2197"></script>


<div class="row"  style="margin-top: 0;">
  <div class="cell" style="width: 45%; padding: 0;">
  <img src="img/twitter-bird-light-bgs.png" width="32" height="32" alt="twitter" style="display: block;" />
  <p class="callout_description">Follow <a href="https://twitter.com/SciPyConf">@SciPyConf</a></p>
</div>

  <div class="cell" style="width: 45%; padding: 0 0 0 1em; border-left: 1px solid #cadbeb;">
  <img src="img/gplus-32.png" width="32" height="32"  alt="g-plus" style="display: block;" />
  <span class="callout_description"><a href="https://plus.google.com/u/0/100948873231627513165/posts">ScipyConference</a></span>
</div>
</div>

  </div>
  <div class="hp_cell" style="margin: 0 2%;">
    <h2>Plan</h2>

      <p>Early-Bird Session Pricing</p>

<table>
  <tr>
    <th>Session </th>
    <th><div align="right">Std Price</div></th>
    <th><div align="right">Academic<br />Price</div></th>
    <th><div align="right">Student<br />Price</div></th>
  </tr>
  <tr>
    <td><strong>Tutorials</strong><br />Jul 6th&nbsp;-&nbsp;7th</td>
    <td align="right"> $ 475</td>
    <td align="right"> $ 375</td>
    <td align="right"> $ 275</td>
  </tr>
  <tr>
    <td><strong>Conference</strong><br />Jul 8th&nbsp;-&nbsp;10th</td>
    <td align="right"> $ 425</td>
    <td align="right"> $ 325</td>
    <td align="right"> $ 225</td>
  </tr>
</table>

<p>Registration will be opening soon.</p>

  </div>
  <div class="hp_cell">
    <h2>Plot</h2>
    <img src="img/plot_contest.png"  width="100%" alt="plot contest"  class="hp_image" />
    <p>In memory of John Hunter, in 2013, we announced the first</p>
    <p style="text-align: center; font-weight: bold;"><a href="../jhepc2013/">SciPy John Hunter Excellence in Plotting Competition</a>.</p>
    <p>We pleased to continue this competition again this year for 2014.</p>
    <p>More details to come.</p>
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