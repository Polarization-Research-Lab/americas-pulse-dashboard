---
layout: datatab
icon: fas fa-handshake
order: 4
---
<script src="{{ site.baseurl }}/assets/js/chartjs-adapter-date-fns.bundle.min.js"></script>

<div id = 'trustval'>

  <div class = 'row chartrow chart trustval-row'>
    <div class='trustval-info '>
      <h2><span class="mr-2">How proud are Americans to be Americans?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
      <p>What we ask:</p>
      <div class="questionbox"><blockquote>How proud are you to be an American?</blockquote></div>
    </div>
    <div class='trustval-line-container'>
      <div class='row trustval-line-div'>
        <canvas id = 'trustval-pride'></canvas>
        <script 
          type="text/javascript" 
          src="{{ site.baseurl }}/assets/js/charts/trustval-line.js" 
          data-canvasid="trustval-pride" 
          data-source="{{ site.baseurl }}/assets/data/trustval/pride.json"
          data-ylabel-4="['Extremely','proud']"
          data-ylabel-3="['Very','proud']"
          data-ylabel-2="['Moderately','proud']"
          data-ylabel-1="['Only a','little proud']"
          data-ylabel-0="['Not at','all proud']"
        ></script>
      </div>
    </div>

  </div>


  <div class = 'row chartrow chart trustval-row'>
    <div class='trustval-info '>
      <h2><span class="mr-2">How much do Americans value the voting process?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
      <p>What we ask:</p>
      <div class="questionbox"><blockquote>How important or unimportant is it to vote in every election?</blockquote></div>
    </div>
    <div class='trustval-line-container'>
      <div class='row trustval-line-div trustval-line-div-alt'>
        <canvas id = 'trustval-vote'></canvas>
        <script 
          type="text/javascript" 
          src="{{ site.baseurl }}/assets/js/charts/trustval-line.js" 
          data-canvasid="trustval-vote" 
          data-source="{{ site.baseurl }}/assets/data/trustval/vote.json"
          data-ylabel-4="['Very','important']"
          data-ylabel-3="['Important']"
          data-ylabel-2="['Neither important','nor unimportant']"
          data-ylabel-1="['Unimportant']"
          data-ylabel-0="['Very','unimportant']"
        ></script>
      </div>
    </div>

  </div>

  <div class = 'row chartrow chart trustval-row'>
    <div class='trustval-info '>
      <h2><span class="mr-2">Do Americans feel their government is responsive?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
      <p>What we ask:</p>
      <div class="questionbox"><blockquote>If you were to complain about the poor quality of a public service, how likely or unlikely is it that the problem would be easily resolved?</blockquote></div>
    </div>
    <div class='trustval-line-container'>
      <div class='row trustval-line-div'>
        <canvas id = 'trustval-response'></canvas>    
        <script 
          type="text/javascript" 
          src="{{ site.baseurl }}/assets/js/charts/trustval-line.js" 
          data-canvasid="trustval-response" 
          data-source="{{ site.baseurl }}/assets/data/trustval/response.json"
          data-ylabel-0="['Extremely','unlikely']"
          data-ylabel-1="['Unlikely']"
          data-ylabel-2="['Equally likely to','or unlikely']"
          data-ylabel-3="['Likely']"
          data-ylabel-4="['Extremely','likely']"
        ></script>
      </div>
    </div>

  </div>

  <div class = 'row chartrow chart trustval-row'>
    <div class='trustval-info '>
      <h2><span class="mr-2">Do Americans trust their politicians?</span><a href="#" class="anchor text-muted"><i class="fas fa-hashtag"></i></a></h2>
      <p>What we ask:</p>
      <div class="questionbox"><blockquote>If a member of Congress were offered a bribe to influence the awarding of a government contract, do you think that the member of Congress would accept or refuse the bribe?</blockquote></div>
    </div>
    <div class='trustval-line-container'>
      <div class='row trustval-line-div trustval-line-div-alt'>
        <canvas id = 'trustval-corruption'></canvas>    
        <script 
          type="text/javascript" 
          src="{{ site.baseurl }}/assets/js/charts/trustval-line.js" 
          data-canvasid="trustval-corruption" 
          data-source="{{ site.baseurl }}/assets/data/trustval/corruption.json"
          data-ylabel-4="['Extremely likely','to refuse']"
          data-ylabel-3="['Likely','to refuse']"
          data-ylabel-2="['Equally likely to','refuse or accept']"
          data-ylabel-1="['Likely','to accept']"
          data-ylabel-0="['Extremely likely','to accept']"
        ></script>
      </div>
    </div>



  </div>

</div>
