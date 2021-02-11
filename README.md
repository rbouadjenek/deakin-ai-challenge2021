# Welcome to the Deakin Simpsons Challenge 2021




<p align="center">
  <img src="images/Simpsons_cast.png">
</p>

The aim of the **Deakin Simpsons challenge 2021** is to identify Simpsons characters individually from images using a machine learning model. Specifically, your goal is to identify the following characters:

<table>
<tr>
  <td> 1. <a href="https://en.wikipedia.org/wiki/Grampa_Simpson" target="_blank" > Abraham grampa Simpson</a> </td>
    <td>11.  <a href="https://simpsons.fandom.com/wiki/Lenny_Leonard" target="_blank" > Lenny Leonard </a> </td>
</tr>
<tr>
      <td> 2. <a href="https://en.wikipedia.org/wiki/Apu_Nahasapeemapetilon" target="_blank" > Apu Nahasapeemapetilon</a> </td>
    <td>12.  <a href="https://en.wikipedia.org/wiki/Lisa_Simpson" target="_blank" > Lisa Simpson </a> </td>
</tr>
<tr>
      <td> 3. <a href="https://en.wikipedia.org/wiki/Bart_Simpson" target="_blank" > Bart Simpson</a> </td>
    <td>13.  <a href="https://en.wikipedia.org/wiki/Marge_Simpson" target="_blank" > Marge Simpson </a> </td>
</tr>
<tr>
      <td> 4. <a href="https://en.wikipedia.org/wiki/Mr._Burns" target="_blank" > Charles Montgomery burns</a> </td>
    <td>14.  <a href="https://en.wikipedia.org/wiki/Mayor_Quimby" target="_blank" > Mayor Quimby </a> </td>
</tr>
<tr>
      <td> 5. <a href="https://en.wikipedia.org/wiki/Chief_Wiggum" target="_blank" > Chief Wiggum</a> </td>
    <td>15.  <a href="https://en.wikipedia.org/wiki/Milhouse_Van_Houten" target="_blank" > Milhouse Van Houten </a> </td>
</tr>
<tr>
      <td> 6. <a href="https://en.wikipedia.org/wiki/Comic_Book_Guy" target="_blank" > Comic Book Guy</a> </td>
    <td>16.  <a href="https://en.wikipedia.org/wiki/Moe_Szyslak" target="_blank" > Moe Szyslak </a> </td>
</tr>
<tr>
      <td> 7. <a href="https://en.wikipedia.org/wiki/Edna_Krabappel" target="_blank" > Edna Krabappel</a> </td>
    <td>17.  <a href="https://en.wikipedia.org/wiki/Ned_Flanders" target="_blank" > Ned Flanders </a> </td>
</tr>
<tr>
      <td> 8. <a href="https://en.wikipedia.org/wiki/Homer_Simpson" target="_blank" > Homer Simpson</a> </td>
    <td>18.  <a href="https://en.wikipedia.org/wiki/Nelson_Muntz" target="_blank" > Nelson Muntz </a> </td>
</tr>
<tr>
      <td> 9. <a href="https://en.wikipedia.org/wiki/Kent_Brockman" target="_blank" > Kent Brockman</a> </td>
    <td>19.  <a href="https://en.wikipedia.org/wiki/Principal_Skinner" target="_blank" > Principal Skinner </a> </td>
</tr>
<tr>
      <td> 10. <a href="https://en.wikipedia.org/wiki/Krusty_the_Clown" target="_blank" > Krusty the Clown</a> </td>
    <td>20.  <a href="https://en.wikipedia.org/wiki/Sideshow_Bob" target="_blank" > Sideshow bob </a> </td>
</tr>
</table>


To achieve this task, you will be given a data set that consists of 19,548 labeled images to train your model and tune your hyperparameters. However, feel free to extend it by collecting new images or by using data augmentation techniques.

Once you have built your model, you will have to submit it on the [CodaLab](https://competitions.codalab.org/competitions/27191?secret_key=f0a7cc3e-7f78-4bb1-8564-95bc2fadafa5) platform to be evaluated. 
We evaluate the performance of your model using the [Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)  on a private test set that we have directly collected and labeled from TV show episodes.
Once the evaluation completed, your entry will appear on the leaderboard to see your performance against other competitors.


In the Notebook that we provide for starting, we will take you through  a 6-step process to build a simple model to perform this task as follows:

1. `Setup the environment:` Thie first step consists of setting the environement and downloading the data.
2. `Preprocessing:` The second step is a preprocessing step that consists of resizing, plitting, and piping the input data.
3. `Exploring the data:` The third step consists of a simple data exploration step where you will see samples of the data and some statistics to help you in understanding the data.
4. `Designing the model:` The forth step consists of designing an architecture for the task.
5. `Traning:` The fifth step consists of starting the training process.
6. `Monitoring:` The sixth step consists of monitoring the traning process to investigate possible overfitting.
7. `Submission:` The seventh and last step will take you through the submission process.

# Timeline
- `15.03.21:` Contest and Phase 1 Begin (Validation Leaderboard opens).
- `15.05.21:` Phase 2 Begin (Testing Leaderboard opens) 🚨 **ONLY ONE SUBMISSION IS ALLOWED FOR THE TEST PHASE! PLEASE MAKE SURE TO SUBMIT YOUR BEST MODEL FROM  PHASE 1!** 🚨.
- `22.05.21:` Last Shot & Contest End.
- `23.05.21:` Semi-Finalists Announcement (top six teams on the Testing Leaderboard).
- `05.06.21:` Report & Code Due.
- `17.06.21:` Winners Announcement.

# Prizes and Sponsors

The winners of the **Deakin Simpsons Challenge 2021** await non-cash prizes worth **AUD1,000** provided by [Deakin University CommUNIty Bank](https://www.bendigobank.com.au/community/universities/community-bank-deakin-university/). The prizes will be distributed among the participants as follows:

- The 1st Place receives a non-cash prize equivalent of **AUD500**.
- The 2nd Place receives a non-cash prize equivalent of **AUD300**.
- The 3rd Place receives a non-cash prize equivalent of **AUD200**.

In order to be eligible for any award, the semi-finalists are required to:

- 🚨 Achieve at least **80%** accuracy for the test phase.
- 🚨 Submit a report, which describes the solution by the stipulated deadline  (4 pages **maximum**, using the [Master Article Template – LaTeX](https://www.overleaf.com/latex/templates/acm-conference-proceedings-master-template/pnrfvrrdbfwt), with the “sigconf” option). Please use the following [easychair link](https://easychair.org/conferences/?conf=deakinsimpsonschallenge2021) to submit your report. The reports will eventually be made publicly available on the website.
- 🚨 Provide a link of the Github repo of the solution in the report. The submitted codes and reports may be inspected to check the validity of the solution. 



The prize money for the challenge is provided by [Deakin University CommUNIty Bank](https://www.bendigobank.com.au/community/universities/community-bank-deakin-university/), Australia.


<img style="float: left;" src="https://cia.communityenterprisefoundation.com.au/Program/GetLogo/20">



# Organizer

The Deakin Simpsons Challenge 2021 is organized by the [School of Information Technology](https://www.deakin.edu.au/information-technology), Faculty of Sci Eng & Built Env (SEBE) at [Deakin University](https://www.deakin.edu.au/). 
<p>
  <img style="float: left;" src="images/deakin2.png" width="200" >
</p>

# Are you competitive enough to participate?

Follow these steps:

1. Register to the [CodaLab](https://competitions.codalab.org/accounts/signup/?next=/) platform.
2. Register to the competition on [CodaLab](https://competitions.codalab.org/competitions/27191?secret_key=f0a7cc3e-7f78-4bb1-8564-95bc2fadafa5).
3. You can participate individually or in a team. To find team members, you can post a message on the discussion forum on [CodaLab](https://competitions.codalab.org/competitions/27191?secret_key=f0a7cc3e-7f78-4bb1-8564-95bc2fadafa5). Once you have built your team, the team leader needs to contact [Mohamed Reda Bouadjenek](https://rbouadjenek.github.io/) with the names of the members, the Deakin course in which they are enrolled, and the name of the team.
4. Please [fork this GitHub repository](https://github.com/rbouadjenek/deakin-simpsons-challenge2020/fork) and make it **private**. Then, click here to open the Notebook in Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rbouadjenek/deakin-simpsons-challenge2020/blob/main/deakin_ai_challenge_training.ipynb). 
5. Just follow the instructions!

We wish you all the best!


# Questions?

- Please first go through all the pages in this competition for complete information.
- If you have further questions, please post them on the Forum tab.





# References

- [The Simpsons characters recognition and detection using Keras](https://medium.com/alex-attia-blog/the-simpsons-character-recognition-using-keras-d8e1796eae36).



# Acknowledgment



Technical design and development by:

**Mohamed Reda Bouadjenek**

**Lecturer of Applied Artificial Intelligence**

**School of Information Technology, Faculty of Sci Eng & Built Env**

**Deakin University**

**Locked Bag 20000, Geelong, VIC 3220**

**reda.bouadjenek@deakin.edu.au**

**www.deakin.edu.au**
<!---
<p>
  <img style="float: left;" src="images/deakin2.png" width="200" >
</p>
--->


<p>
  <a href="https://twitter.com/DeakinAI2021" > <img style="float: left;" src="https://irisconnect.com/uk/wp-content/uploads/sites/3/2020/12/twitter-Follow-us-button.png" width="200" > </a>
</p>
