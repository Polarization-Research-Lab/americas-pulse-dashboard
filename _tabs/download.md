---
layout: downloads
order: 5
icon: fas fa-info-circle
---

<h1 class = 'text-center'>Downloads</h1>

<div class = 'row'>
  <div class = 'col-6'>
    <div class = 'dl'>
      <h3 class = 'dlh3'>All Data Collected (so far)</h3>
      <button id='download-btn-all'>Download All Survey Data</button>
    </div>
  </div>

  <div class = 'col-6'>
    <div class = 'dl'>
      <h3 class = 'dlh3'>Survey Data by Week</h3>
      <p>Select a week: 
      <select id='dlselectbox'>
        {% for data in site.data.datalinks %}
        <option value="{{ data.file }}" data-week="{{ data.week }}" data-year="{{ data.year }}">
          {{ data.year }} - week {{ data.week }}
        </option>
        {% endfor %}
      </select></p>
      <button id='download-btn-week'>Download Data File</button>
      <button id='download-btn-week-topline'>Download Topline Report</button>
    </div>
  </div>
</div>


<br>
<hr>
<br>

The [America's Pulse Survey](https://polarizationresearchlab.org/americas-political-pulse/) is collected each week using participants from the [YouGov panel](https://yougov.com/).

A specific description of each variable in the survey can be found [here](https://drive.google.com/file/d/1S5b3-OyktijpSs46QCWwwtOqJjYZtQ0U/view?usp=share_link).

\*Data is distributed under the <a href="https://creativecommons.org/licenses/by-sa/4.0/">Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License</a>.


## Citation

If you use our data in your research, we humbly ask that you cite our lab 🙏:

> Shanto Iyengar, Yphtach Lelkes and Sean Westwood. (2023). America’s Political Pulse. https://polarizationresearchlab.org/americas-political-pulse/.


## Notes

### How do I calculate "Affective Polarization"?

In our research (and on our public visualizations), we calculate "affective polarization" exactly as follows:

1. Define Democrats as anyone where `pid7` is 1, 2, or 3
2. Define Republicans as anyone where `pid7` is between 5, 6, or 7
3. Remove everyone where `pid7` equals 4
4. Remove any rows with missing values in the `republican_therm_1` and `democrat_therm_1` columns (there shouldn't be many)
5. For Democrats, calculate: `democrat_therm_1 - republican_therm_1`
6. For Republicans, calculate: `republican_therm_1 - democrat_therm_1`
7. Remove anyone with a negative score

### The `starttime` and `endtime` Variables

The start and end time columns mark when a participant starts and finishes our survey. We often find that participants start our survey to claim a spot in the YouGov panel, but then opt to finish the bulk of the survey later. For this reason, we often use end times for any time-series analyses.

### The `engagement_measure` Variable

For the engagement measure, we show participants a passage about a wildlife funding program for a particular state. The passage is then removed, and participants are asked what state (of 7 possible options) the passage referred to. We've recoded this data to label participants as "engaged" or "not engaged" based on whether they guessed the correct state.

<script src="{{ site.baseurl }}/assets/js/download-btn.js"></script>
