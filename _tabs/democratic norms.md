---
layout: datatab
icon: fas fa-landmark
order: 2
---

<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>

<br>
<br>
<h2><span class="mr-2">3Do Americans support Violations of Democratic Norms?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
<p>The strength of a democracy depends on the willingness of citizens and elites to respect democratic norms and institutions.</p>

<h3>Average Number of Norm Violations Supported (by Region)</h3>

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
<div class = 'row chartrow violence-row violence-row-alt'>
  <div class='chartv'>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>Do you agree or disagree: {inparty: Democratic/Republican} elected officials should sometimes consider ignoring court decisions when the judges who issued those decisions were appointed by {outparty: Democratic/Republican} presidents.</blockquote></div>
  </div>
  <div class = 'violence-line-container'>
    <div class='row violence-line-div'>
      <canvas id = 'demnorm-judges'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-judges" data-source='{{ site.baseurl }}/assets/data/norms/norm_judges.json'></script>
    </div>
  </div>
</div>

<h5>Support for Reducing Polling Stations</h5>
<div class = 'row chartrow violence-row violence-row-alt'>
  <div class='chartv'>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>Do you agree or disagree: {inparty: Democrats/Republicans} should reduce the number of polling stations in areas that typically support {outparty: Democrats/Republicans}.</blockquote></div>
  </div>
  <div class = 'violence-line-container'>
    <div class='row violence-line-div'>
      <canvas id = 'demnorm-polling'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-polling" data-source='{{ site.baseurl }}/assets/data/norms/norm_polling.json'></script>
    </div>
  </div>
</div>

<h5>Support for Using Executive Orders to Circumvent Congress</h5>
<div class = 'row chartrow violence-row violence-row-alt'>
  <div class='chartv'>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>Do you agree or disagree: If a {inparty: Democratic/Republican} president can't get cooperation from {outparty: Democratic/Republican} members of congress to pass new laws, the {inparty: Democratic/Republican} president should circumvent Congress and issue executive orders on their own to accomplish their priorities.</blockquote></div>
  </div>
  <div class = 'violence-line-container'>
    <div class='row violence-line-div'>
      <canvas id = 'demnorm-executive'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-executive" data-source='{{ site.baseurl }}/assets/data/norms/norm_executive.json'></script>
    </div>
  </div>
</div>

<h5>Suport for Media Censorship</h5>
<div class = 'row chartrow violence-row violence-row-alt'>
  <div class='chartv'>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>Do you agree or disagree with the following: The government should be able to censor media sources that spend more time attacking {inparty: Democrats/Republicans} than {outparty: Democrats/Republicans}.</blockquote></div>
  </div>
  <div class = 'violence-line-container'>
    <div class='row violence-line-div'>
      <canvas id = 'demnorm-censorship'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-censorship" data-source='{{ site.baseurl }}/assets/data/norms/norm_censorship.json'></script>
    </div>
  </div>
</div>

<h5>Support for Constitution in the Face of Election Denial</h5>
<div class = 'row chartrow violence-row violence-row-alt'>
  <div class='chartv'>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>Do you agree or disagree with the following: When a {inparty: Democratic/Republican} candidate questions the outcome of an election other {inparty: Democrats/Republicans} should be more loyal to the {inparty: Democratic/Republican} party than to election rules and the constitution.</blockquote></div>
  </div>
  <div class = 'violence-line-container'>
    <div class='row violence-line-div'>
      <canvas id = 'demnorm-loyalty'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-loyalty" data-source='{{ site.baseurl }}/assets/data/norms/norm_loyalty.json'></script>
    </div>
  </div>
</div>
