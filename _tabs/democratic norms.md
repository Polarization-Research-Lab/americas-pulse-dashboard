---
layout: datatab
icon: fas fa-landmark
order: 2
---

<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>


<div class = 'row' id='demnorm-row-1'>

    <div class='col-3' id='demnorm-title'>
      <h2><span class="mr-2">Do Americans support Violations of Democratic Norms?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
      <p>The strength of a democracy depends on the willingness of citizens and elites to respect democratic norms and institutions.</p>
      <p>Each week, we ask Americans which norms, if any, they would support elected officials violating.</p>
    </div>

    <div class = 'col-6'>
      <h3 class = 'text-center'>Avg # of Norm Violations Supported (by Region)</h3>
      <div class = 'col-6' id='demnorm-map-div'>
        <canvas id='demnorm-map'></canvas>
        <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/map.js" data-canvasid="demnorm-map"  data-source="{{ site.baseurl }}/assets/data/demnorm-map.json" data-scaleminlabel = "Less" data-scalemaxlabel = "More"></script>
      </div>
    </div>

</div>


<div class = 'row' id='demnorm-row-2'>

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

</div>



<div class = 'row chartrow chart' id='demnorm-row-3'>
  
  <div id='SupportPartyHeader'><h2><span class="mr-2">Support for Norm Violations by Party.</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2></div>

  <div class='norm-chart-container'>
    <div class='row col-8 norm-row'>

      <div class='col-4'> 
        <div class = 'norm-chart-div-parent'>
          <div class = 'norm-chart-div'>
            <canvas id = 'demnorm-judges'></canvas>
          </div>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-judges" data-source='{{ site.baseurl }}/assets/data/norms/norm_judges.json'></script>
          <div class='norm-party-header'><h3 class='text-center'>Support for Ignoring Court Judges</h3></div>
        </div>
      </div>


      <div class='col-4'> 
        <div class = 'norm-chart-div-parent'>
          <div class = 'norm-chart-div'>
            <canvas id = 'demnorm-polling'></canvas>
          </div>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-polling" data-source='{{ site.baseurl }}/assets/data/norms/norm_polling.json'></script>
          <div class='norm-party-header'><h3 class='text-center'>Support for Reducing the # of Polling Stations</h3></div>
        </div>
      </div>
    </div>
    <div class='row col-8 norm-row'>
      <div class='col-4'> 

        <div class = 'norm-chart-div-parent'>
          <div class = 'norm-chart-div'>
            <canvas id = 'demnorm-executive'></canvas>
          </div>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-executive" data-source='{{ site.baseurl }}/assets/data/norms/norm_executive.json'></script>
          <div class='norm-party-header'><h3 class='text-center'>Support for Using Executive Orders</h3></div>
        </div>
      </div>


   

    <br>

    <div class='row col-8 justify-content-center norm-row'>

      <div class='col-4'> 
        <div class = 'norm-chart-div-parent'>
          <div class = 'norm-chart-div'>
            <canvas id = 'demnorm-censorship'></canvas>
          </div>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-censorship" data-source='{{ site.baseurl }}/assets/data/norms/norm_censorship.json'></script>
          <div class='norm-party-header'><h3 class='text-center'>Suport for Censorship</h3></div>
        </div>
      </div>

    </div>
    <div class='row col-8 norm-row'>
      <div class='col-4'> 
        <div class = 'norm-chart-div-parent'>
          <div class = 'norm-chart-div'>
            <canvas id = 'demnorm-loyalty'></canvas>
          </div>
          <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/demnorm-party.js" data-canvasid="demnorm-loyalty" data-source='{{ site.baseurl }}/assets/data/norms/norm_loyalty.json'></script>
          <div class='norm-party-header'><h3 class='text-center'>Support for Party Loyalty in the Face of Election Denial</h3></div>
        </div>
      </div>


    </div>
  </div>
</div>
