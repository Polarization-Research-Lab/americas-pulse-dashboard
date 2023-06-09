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
<div class='row chartrow chart' id='affpol-row-1'>

  <!-- info -->
  <div class='col-4' id='affpol-row-1-info'>
    <h2><span class="mr-2">Affective Polarization in the US</span><a href="#affective-polarization-in-the-us" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <p>Each week, we ask a thousand Americans how they feel about their own political party, as well as how they feel about the opposing political party. We define <emph>polarization</emph> as the difference between the two <sup><a href = "https://academic.oup.com/poq/article-abstract/76/3/405/1894274">[Iyengar et al., 2012]</a></sup>.</p>
<!-- 
    <h3 class = 'gauge-heading'>National Average:</h3>
    <canvas id = 'affpol-nat-avg' class='gauge'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-nat-avg" data-gauge="{{ site.data.meta.affpol_nat_avg }}"></script>
    <p class = 'text-center'>{{ site.data.meta.affpol_nat_avg }}%</p>
 -->
    <div class = "row">
      <div class = 'col-6'>
        <h3 class = 'gauge-heading'>Democrats:</h3>
        <div class = 'gauge-div'>
          <canvas id = "affpol-dem-avg" class="gauge"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-dem-avg" data-gauge="{{ site.data.meta.affpol_dem_avg }}"></script>
          <p class = 'text-center'>{{ site.data.meta.affpol_dem_avg }}%</p>
        </div>
      </div>

      <div class = 'col-6'>
        <h3 class = 'gauge-heading'>Republicans:</h3>
        <div class = 'gauge-div'>
          <canvas id = "affpol-rep-avg" class="gauge"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-rep-avg" data-gauge="{{ site.data.meta.affpol_rep_avg }}"></script>
          <p class = 'text-center'>{{ site.data.meta.affpol_rep_avg }}%</p>
        </div>
      </div>

    </div>
  </div>

  <div class='col-8'>
    <div class='row' id='affpol-map-div'>
      <canvas id = "affpol-map" class=""></canvas>
      <script src='{{ site.baseurl }}/assets/js/charts/map.js' data-canvasid="affpol-map" data-source="{{ site.baseurl }}/assets/data/affpol-map.json" data-scaleminlabel = "Less" data-scalemaxlabel = "More"></script>
    </div>


  </div>

</div>

<div class = 'row chartrow chart' id='affpol-row-2'>

    <div class='col-9' id='affpol-time-div'>
      <canvas id = "affpol-time" class=""></canvas>
      <script src='{{ site.baseurl }}/assets/js/charts/affpol-time.js' data-canvasid="affpol-time"></script>
    </div>

    <div class='col-3' id='affpol-time-info'>
        <h2><span class="mr-2">Is it getting better or worse?</span><a href="#is-it-getting-better-or-worse?" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
        <p>The y-axis shows the level of polarization, averaged across each week.</p>
        <!-- <p>Our national sample's average amount of polarization is <b>{{ site.data.meta.affpol_nat_avg }}</b>.</p> -->
        <!-- <p>The average from our last survey was <b>{{ site.data.meta.affpol_nat_avg }}</b>.</p> -->
        <div id = "affpol-timebar-div" >
          <!-- <h3>Past 3 weeks:</h3> -->
          <canvas id = "affpol-timebar" class=""></canvas>
        <script src='{{ site.baseurl }}/assets/js/charts/affpol-timebar.js' data-canvasid="affpol-timebar" data-thisweek="{{ site.data.meta.thisweek }}" data-lastweek="{{ site.data.meta.lastweek }}" data-2weeksago="{{ site.data.meta.twoweeksago}}"></script>
        </div>
    </div>

</div> <!-- end row2 -->


<!-- row 3 -->
<div class = 'row chartrow chart' id='affpol-row-3'>

  <!-- info -->
  <div class='col-3' id='affpol-hist-info'>
    <div class = 'd-flex p-2'>

      <img class = 'icon-title' src = '{{ site.baseurl }}/assets/img/home-therm.png'>

      <h2><span class="mr-2">Which party is more polarized?</span><a href="#which-party-is-worse" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    </div>

    <p><b>Top:</b> How <emph>Democrats</emph> rate the Republican and Democratic Party</p>
    <p><b>Bottom:</b> How <emph>Republicans</emph> rate the Republican and Democratic Party</p>
    <p><b>Vertical dashed line:</b> Average</p>
  </div>

  <div class='col-9 row d-flex justify-content-center' id='affpol-hists'>

    <div class='col-12 affpol-hist-container'>

      <div class=''>
        <h3 class = 'text-center'>Democrats</h3>
        <br>
        <div class='col-12 affpoll-hist-div'>
          <canvas id = "affpol-dem-hist" class="affpol-hist"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/affpol-hist.js" data-canvasid="affpol-dem-hist" data-source="{{ site.baseurl }}/assets/data/affpol-hist-dem.json"></script>
        </div> 
      </div> 

      <!-- <div class='col-2'>
        <div>
          <canvas id = "affpol-dem-avg2" class="gauge"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-dem-avg2" data-gauge="{{ site.data.meta.affpol_dem_avg }}"></script>
        </div> 
      </div>  -->

    </div>

    <hr>

    <div class='col-12 affpol-hist-container'>
      
      <div class=''>
        <h3 class = 'text-center'>Republicans</h3>
        <br>
        <div class='col-12 affpoll-hist-div'>
          <canvas id = "affpol-rep-hist" class="affpol-hist"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/affpol-hist.js" data-canvasid="affpol-rep-hist" data-source="{{ site.baseurl }}/assets/data/affpol-hist-rep.json"></script>
        </div> 
      </div> 

      <!-- <div class='col-2'>
        <div>
          <canvas id = "affpol-rep-avg2" class="gauge"></canvas>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/gauge.js" data-canvasid="affpol-rep-avg2" data-gauge="{{ site.data.meta.affpol_rep_avg }}"></script>
        </div> 
      </div>  -->

    </div>

  </div>

</div> <!-- end row3 -->
