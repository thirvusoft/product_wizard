## Product Wizard
<h4><b> Product List </b></h4>
<a href="#1.User Not Allowed When Subscription End Date ">1.User Not Allowed When Subscription End Date </a>
<br>
<p> File Path: apps/product_wizard/product_wizard/product_wizard/backup_files/auth.py </p>
<p> Function: authenticate </p>
<div id="1.User Not Allowed When Subscription End Date ">
<p> Modification : Get Customer List and Compare Login User And Customer User Id is Same </p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;then check condition satisfied and get Subscription List of customer and <p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;taken the end date of subscription of customer and check this end date was grater than<p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;today date, the condition will satisfied throw the message to login process <p>
</div>
<br>
<a href="#2.User Location Adding in Activity Log ">2.User Location Adding in Activity Log </a>
<p> File Path: apps/product_wizard/product_wizard/product_wizard/backup_files/activity_log.py </p>
<p> Function: add_authentication_log</p>
<p> Modification: Install geocoder Package and get user ip then get lat long list and it </p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; get location of ip lat long </p>
<h4><b> Outof Box Burst Out</b></h4>
