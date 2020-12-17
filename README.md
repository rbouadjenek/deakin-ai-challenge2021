# Welcome to the Deakin Simpsons Challenge 2021


<p align="center">
  <img src="images/Simpsons_cast.png">
</p>

The aim of the Deakin Simpsons challenge 2021 is to identify Simpsons characters individually from pictures using a machine learning model. Specifically, your goal is to identify the following characters:

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


To achieve this task, you will be given a data set that consists of 19,548 images to train your model and tune your hyperparameters. However, feel free to extend it by collecting new images or by using data augmentation techniques.

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

- xx.xx.21 Contest and Phase 1 Begin (Validation Leaderboard opens)
- xx.xx.21 Phase 2 Begin (Testing Leaderboard opens)
- xx.xx.21 Last Shot & Contest End
- xx.xx.21 Semi-Finalists Announcement (top six teams on the Testing Leaderboard)
- xx.xx.21 Report & Code Due
- xx.xx.21 Winners Announcement

# Prizes and Sponsors

The winners of the Deakin Simpsons Challenge 2021 await prizes worth AUDXYZ provided by YYZ and YYZ. The prizes will be distributed among the participants as follows:

- The 1st Place receives a prize of AUDXXX.
- The 2nd Place receives a prize of AUDXXX.
- The 3rd Place receives a prize of AUDXXX.

In order to be eligible for any award, the semi-finalists are required to submit the code and solution report (4 pages) to the organizers by the stipulated deadline. The submitted codes and reports may be inspected to check the validity of the solution. The reports will eventually be made publicly available on the website.

The complete list of sponsors includes:
- XYZ.
- XYZ.
- XYZ.

# Do you want to try?

Please [fork this GitHub repository](https://github.com/rbouadjenek/deakin-simpsons-challenge2020/fork). Then, click here to open the Notebook in Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rbouadjenek/deakin-simpsons-challenge2020/blob/main/deakin_ai_challenge_training.ipynb). 

Just follow the instructions!

# Questions?

- Please first go through all the pages in this competition for complete information.
- If you have further questions, please post them on the Forum tab.

We wish you all the best!




# References

- [The Simpsons characters recognition and detection using Keras](https://medium.com/alex-attia-blog/the-simpsons-character-recognition-using-keras-d8e1796eae36).



# Acknowledgment

**Mohamed Reda Bouadjenek**

**Lecturer of Applied Artificial Intelligence**

**School of Information Technology, Faculty of Sci Eng & Built Env**

**Deakin University**

**Locked Bag 20000, Geelong, VIC 3220**

**reda.bouadjenek@deakin.edu.au**

**www.deakin.edu.au**

<img style="float: left;" src="images/deakin2.png" width="200" >
