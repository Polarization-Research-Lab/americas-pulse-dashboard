---
layout: datatab
icon: fas fa-face-angry
order: 1
params: 
  # variable name: type (checkbox, slider, interval slider)
  use_subj_weights: checkbox
---

<script type="text/javascript" src='{{ site.baseurl }}/assets/js/gauge.js'></script>
<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/chartjs-plugin-annotation.min.js"></script>

<!-- row 1 -->
<br>
<br>
<h2>3<span class="mr-2">Affective Polarization in the US</span><a href="#affective-polarization-in-the-us" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
<p>Each week, we ask a thousand Americans how they feel about their own political party, as well as how they feel about the opposing political party. <emph>Affective polarization</emph> is the difference between the two <sup><a href = "https://academic.oup.com/poq/article-abstract/76/3/405/1894274">[Iyengar et al., 2012]</a></sup>.</p>

<h3>Affective polarization by state</h3>
<div class='row chartrow chart' id='affpol-row-1'>
    <div class='row' id='affpol-map-div'>
      <canvas id = "affpol-map" class=""></canvas>
      <script src='{{ site.baseurl }}/assets/js/charts/map.js' data-canvasid="affpol-map" data-source="{{ site.baseurl }}/assets/data/affpol-map.json" data-scaleminlabel = "Less" data-scalemaxlabel = "More"></script>
  </div>
</div>


<h3>Avergae level of polarizaiton by party</h3>
<p>(more is worse)</p>
<div class = 'row chartrow chart'>
  <div class = 'col-4'>
    <h5 class = 'gauge-heading'>Democrats:</h5>
    <div class = 'gauge-div'>
      <canvas id = "affpol-dem-avg" class="gauge"></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-dem-avg" data-gauge="{{ site.data.meta.affpol_dem_avg }}"></script>
      <p class = 'text-center'>{{ site.data.meta.affpol_dem_avg }}</p>
    </div>
  </div>

  <div id = 'col1'>
    <p>&nbsp;</p>
  </div>

  <div class = 'col-4'>
    <h5 class = 'gauge-heading'>Republicans:</h5>
    <div class = 'gauge-div'>
      <canvas id = "affpol-rep-avg" class="gauge"></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-rep-avg" data-gauge="{{ site.data.meta.affpol_rep_avg }}"></script>
      <p class = 'text-center'>{{ site.data.meta.affpol_rep_avg }}</p>
    </div>
  </div>

</div><!-- end row2 -->
<h3>Is it getting better or worse?<a href="#is-it-getting-better-or-worse?" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h3>
<p>Affective polarization averaged across each week.</p>
<div class = 'row chartrow chart' id='affpol-row-3'>
    <div id='affpol-time-div'>
      <canvas id = "affpol-time" class=""></canvas>
      <script src='{{ site.baseurl }}/assets/js/charts/affpol-time.js' data-canvasid="affpol-time"></script>
    </div>
    <!-- <div class='col-1' id='affpol-time-info'>
        <div id = "affpol-timebar-div" >
          <h3>Past 3 weeks:</h3>
          <canvas id = "affpol-timebar" class=""></canvas>
        <script src='{{ site.baseurl }}/assets/js/charts/affpol-timebar.js' data-canvasid="affpol-timebar" data-thisweek="{{ site.data.meta.thisweek }}" data-lastweek="{{ site.data.meta.lastweek }}" data-2weeksago="{{ site.data.meta.twoweeksago}}"></script>
        </div>
    </div> -->

</div> <!-- end row3 -->


<!-- row 4 -->
<div class = 'row chartrow chart' id='affpol-row-4'>
  <h3><span class="mr-2">Which party is more polarized?</span><a href="#which-party-is-worse" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h3>
  
  <div class='row d-flex justify-content-center' id='affpol-hists'>
    <div class='affpol-hist-container'>
      <div class=''>
        <h5 class = 'text-center'>Democrats</h5>
        <br>
        <div class='affpoll-hist-div'>
          <canvas id = "affpol-dem-hist" class="affpol-hist"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/affpol-hist.js" data-canvasid="affpol-dem-hist" data-source="{{ site.baseurl }}/assets/data/affpol-hist-dem.json"></script>
        </div> 
      </div> 
    </div>
    <hr>
    <div class='affpol-hist-container'>
      <div class=''>
        <h5 class = 'text-center'>Republicans</h5>
        <br>
        <div class='affpoll-hist-div'>
          <canvas id = "affpol-rep-hist" class="affpol-hist"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/affpol-hist.js" data-canvasid="affpol-rep-hist" data-source="{{ site.baseurl }}/assets/data/affpol-hist-rep.json"></script>
        </div> 
      </div> 
    </div>
    <p><b>Vertical dashed line:</b> Average</p>
  </div>

</div> <!-- end row3 -->
