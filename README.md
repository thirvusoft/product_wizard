## Product Wizard
<h4><b> Product List </b></h4>
<h5><b>1.User Not Allowed When Subscription End Date </b></h5>
<p> File Path: apps/product_wizard/product_wizard/product_wizard/backup_files/auth.py </p>
<p> Function: authenticate </p>
<p> Modification : Get Customer List and Compare Login User And Customer User Id is Same </p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;then check condition satisfied and get Subscription List of customer and <p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;taken the end date of subscription of customer and check this end date was grater than<p>
<p>&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;today date, the condition will satisfied throw the message to login process <p>
