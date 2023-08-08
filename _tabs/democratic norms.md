---
layout: datatab
icon: fas fa-landmark
order: 2
---

<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>

<br>
<br>
<h2><span class="mr-2">2Do Americans support Violations of Democratic Norms?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
<p>The strength of a democracy depends on the willingness of citizens and elites to respect democratic norms and institutions.</p>
<p>Each week, we ask Americans which norms, if any, they would support elected officials violating.</p>
<h3 class = 'text-center'>Avg # of Norm Violations Supported (by Region)</h3>

<div class='row chartrow chart' id='affpol-row-1'>
  <div class='row' id='affpol-map-div'>
    <canvas id='demnorm-map'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/map.js" data-canvasid="demnorm-map"  data-source="{{ site.baseurl }}/assets/data/demnorm-map.json" data-scaleminlabel = "Less" data-scalemaxlabel = "More"></script>
    </div>
  </div>

<!-- <div class = 'row' id='demnorm-row-2'>
    <div class='row col-6' id='demnorm-lines-div'>
      <canvas id = 'demnorm-lines'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-lines.js" data-canvasid="demnorm-lines"></script>
      <div id="demnorms-legend" style='background-color: red;'></div>
    </div>
    <div class='row col-3'>
      <div id = 'demnormline-btn-div'>
        <div class = 'demnormline-btn-wrap'><button data-index='0' class="demnormline-btn">Ignoring Supreme Court Judges</button></div>
        <div class = 'demnormline-btn-wrap'><button data-index='1' class="demnormline-btn">Reducing the # of Polling Stations</button></div>
        <div class = 'demnormline-btn-wrap'><button data-index='2' class="demnormline-btn">Using Executive Orders</button></div>
        <div class = 'demnormline-btn-wrap'><button data-index='3' class="demnormline-btn">Censorship</button></div>
        <div class = 'demnormline-btn-wrap'><button data-index='4' class="demnormline-btn">Party Loyalty in the Face of Election Denial</button></div>
      </div>
    </div>
</div> -->


<h2><span class="mr-2">Support for Norm Violations by Party.</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
<h5>Support for Ignoring Court Judges</h5>
<div class = 'row chartrow chart' id='affpol-row-3'>
  <div id='affpol-time-div'>
    <canvas id = 'demnorm-judges'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-judges" data-source='{{ site.baseurl }}/assets/data/norms/norm_judges.json'></script>
  </div>
</div>

<h5>Support for Reducing the # of Polling Stations</h5>
<div class = 'row chartrow chart' id='affpol-row-3'>
  <div id='affpol-time-div'>
    <canvas id = 'demnorm-polling'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-polling" data-source='{{ site.baseurl }}/assets/data/norms/norm_polling.json'></script>
  </div>
</div>

<h5>Support for Using Executive Orders</h5>
<div class = 'row chartrow chart' id='affpol-row-3'>
  <div id='affpol-time-div'>
    <canvas id = 'demnorm-executive'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-executive" data-source='{{ site.baseurl }}/assets/data/norms/norm_executive.json'></script>
    <div class='norm-party-header'>
  </div>
</div>

<h5>Suport for Media Censorship</h5>
<div class = 'row chartrow chart' id='affpol-row-3'>
  <div id='affpol-time-div'>
    <canvas id = 'demnorm-censorship'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-censorship" data-source='{{ site.baseurl }}/assets/data/norms/norm_censorship.json'></script>
    <div class='norm-party-header'>
  </div>
</div>

<h5>upport for Party Loyalty in the Face of Election Denial</h5>
<div class = 'row chartrow chart' id='affpol-row-3'>
  <div id='affpol-time-div'>
    <canvas id = 'demnorm-loyalty'></canvas>
    <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-loyalty" data-source='{{ site.baseurl }}/assets/data/norms/norm_loyalty.json'></script>
    <div class='norm-party-header'>
  </div>
</div>

