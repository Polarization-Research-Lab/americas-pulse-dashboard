---
layout: datatab
icon: fas fa-skull-crossbones
order: 3
---

<script src="{{ site.baseurl }}/assets/js/chartjs-chart-sankey.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>
<script src="{{ site.baseurl }}/assets/js/chartjs-plugin-annotation.min.js"></script>

<div class = 'row chartrow chart' id='violence-row-1'>

  <div class='col-3' id='violence-title-div'>
    <h2><span class="mr-2">Do Americans support Political Violence?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <p>Each week survey, respondents review a series of political acts -- starting with attitudes toward non-violent protests and increasing to support for political murder.</p>
  </div>

  <div class='col-9'>
    <div id='violence-sankey-div'>
      <canvas id = 'violence-sankey'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-sankey.js" data-canvasid="violence-sankey"></script>
    </div>
  </div>

</div>


<div class = 'row chartrow chart violence-row violence-row-alt'>

  <div class='col-9'>
    <div class='row violence-line-div'>
      <canvas id = 'violence-line-protest'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-protest" data-source="{{ site.baseurl }}/assets/data/violence1.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Protesting Without a Permit</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v1question'>{name} was convicted of protesting without a permit. He was arrested by police after leading a protest against {outparty} on the grounds of the county courthouse. He made no effort to acquire the necessary permit for the protest and refused to leave when asked by police. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>


<div class = 'row chartrow chart violence-row'>

  <div class='col-9'>
    <div class='row violence-line-div violence-line-div-alt'>
      <canvas id = 'violence-line-vandalism'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-vandalism" data-source="{{ site.baseurl }}/assets/data/violence2.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Vandalism</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v2question'>{name} was convicted of vandalism. He was arrested by police after he vandalized several large signs expressing support for candidates of the {outparty} party. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>

<div class = 'row chartrow chart violence-row violence-row-alt'>

  <div class='col-9'>
    <div class='row violence-line-div'>
      <canvas id = 'violence-line-assault'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-assault" data-source="{{ site.baseurl }}/assets/data/violence3.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Assault</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v3question'>{name} was convicted of assault. He was arrested by police for throwing rocks at peaceful {outparty} protesters. Although no one was  seriously injured, paramedics bandaged a man with a head wound. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>

<div class = 'row chartrow chart violence-row'>

  <div class='col-9'>
    <div class='row violence-line-div violence-line-div-alt'>
      <canvas id = 'violence-line-arson'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-arson" data-source="{{ site.baseurl }}/assets/data/violence4.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Arson</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v4question'>{name} was convicted of arson. He was arrested by police as he attempted to run from a fire he started at the local {outparty} headquarters. Although he waited for the building to close for the night, several adjacent buildings were still occupied. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>

<div class = 'row chartrow chart violence-row violence-row-alt'>

  <div class='col-9'>
    <div class='row violence-line-div'>
      <canvas id = 'violence-line-assaultdeadly'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-assaultdeadly" data-source="{{ site.baseurl }}/assets/data/violence5.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Assault with a Deadly Weapon</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v5question'>{name} was convicted of assault with a deadly weapon.He was arrested by police after driving his car into a crowd of {outparty} protesters. Although no one was killed, several individuals were seriously injured and one spent a month in the hospital. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>

<div class = 'row chartrow chart violence-row'>

  <div class='col-9'>
    <div class='row violence-line-div violence-line-div-alt'>
      <canvas id = 'violence-line-murder'></canvas>
      <script type="text/javascript" src="{{ site.baseurl }}/assets/js/charts/violence-line.js" data-canvasid="violence-line-murder" data-source="{{ site.baseurl }}/assets/data/violence6.json"></script>
    </div>
  </div>

  <div class='col-3 chart'>
    <h2><span class="mr-2">Support for Murder</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
    <h4>What we ask:</h4>
    <div class="questionbox"><blockquote id='v6question'>{name} was convicted of murder. He was arrested by police after surveillance footage was found showing him stabbing a prominent {outparty} to death. {name} targeted the victim because he believed the victim had prevented him from voting in the last election as part of a conspiracy to stop {inparty} voters. Do you support or oppose {name}’s actions?</blockquote></div>
  </div>

</div>




