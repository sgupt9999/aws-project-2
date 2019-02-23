#!/usr/local/bin/python3.6

import boto3
import sys
import urllib.request
import shutil
from zipfile import ZipFile
from os import listdir
from os.path import join

def create_index_html_file():
## Create index.html document
	file = open('./index.html','w')
	file.write('<!DOCTYPE html>\n')
	file.write('<html lang="en">\n')
	file.write('\n')
	file.write('\n')
	file.write('	<head>\n')
	file.write('\n')
	file.write('\n')
	file.write('		<!-- required meta tags -->\n')
	file.write('		<meta charset="utf-8">\n')
	file.write('		<meta http-equip="X-UA-Compatible" conent="IE=edge">\n')
	file.write('		<meta name="viewport" content="width=device-width, initial-scale=1">\n\n')
	file.write('		<!-- title -->\n')
	file.write('		<title>CMEI Systems Inc.</title>\n\n')
	file.write('		<!-- favicon -->\n')
	file.write('		<link rel="shortcut icon" href="img/favicon.ico">\n')
	file.write('		<!-- google fonts -->\n')
	file.write('		<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Condensed:300,300i,400,400i,700,700i">\n')
	file.write('		<!-- fontawesome -->\n')
	file.write('		<link rel="stylesheet" href="css/font-awesome/css/font-awesome.min.css">\n')
	file.write('		<!-- bootstrap CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/bootstrap/bootstrap.min.css">\n')
	file.write('		<!-- animate CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/animate/animate.css">\n')
	file.write('		<!-- magnific-popup CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/magnific-popup/magnific-popup.css">\n')
	file.write('		<!-- style CSS -->\n')
	file.write('		<link rel="stylesheet" href="css/style.css">\n\n')
	file.write('\n')
	file.write('\n')
	file.write('	</head>\n') ## End of head section


	file.write('\n')
	file.write('\n')
	file.write('	<body>\n')
	file.write('\n')
	file.write('		<!-- Home -->\n')
	file.write('		<section id="home">\n')
	file.write('			<div id="home-cover" class="bg-parallax animated fadeIn">\n')
	file.write('				<div id="home-content-box">\n')
	file.write('					<div id="home-content-box-inner" class="text-center">\n')
	file.write('						<div id="home-heading" class="animated zoomIn">\n')
	#file.write('							<h3>Watch Out <br> The Modern Responsive Website!<h3>\n')
	file.write('							<h3>Coming Soon <br> Aaliya Gupta\'s Amazing Gallery<h3>\n')
	file.write('						</div>\n')
	file.write('						<div id="home-btn" class="animated zoomIn">\n')
	file.write('							<a class="btn btn-lg btn-general btn-white" href="#work" roles="button"\n')
	file.write('							title="View Our Work">View Our Work</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n')
	file.write('		</section>\n\n\n')


	file.write('		<!-- Services -->\n')
	file.write('		<section id="services">\n')
	file.write('			<div class="content-box">\n')
	file.write('				<div class="content-title wow animated fadeInDown" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('					<h3> Services </h3>\n')
	file.write('					<div class="content-title-underline"></div>\n')
	file.write('				</div>\n')
	file.write('				<div class="container">\n')
	file.write('					<div class="row wow animated fadeInUp" data-wow-duration="1s" data-wow-delay=".5s">\n')

	file.write('						<div class="col-md-4">\n')
	file.write('							<div class="service-item">\n')
	file.write('								<div class="service-item-icon">\n')
	file.write('									<i class="fa fa-paint-brush fa-3x"></i>\n')
	file.write('								</div>\n') ##service-item-icon
	file.write('								<div class="service-item-title">\n')
	file.write('									<h3> Web Design </h3>\n')
	file.write('								</div>\n') ##service-item-title
	file.write('								<div class="service-item-desc">\n')
	file.write('									<p>This is service item</p>\n')
	file.write('								</div>\n') ##service-item-desc
	file.write('							</div>\n') ##service-item
	file.write('						</div>\n') ##column

	file.write('            <div class="col-md-4">\n')
	file.write('              <div class="service-item">\n')
	file.write('                <div class="service-item-icon">\n')
	file.write('                  <i class="fa fa-laptop fa-3x"></i>\n')
	file.write('                </div>\n') ##service-item-icon
	file.write('                <div class="service-item-title">\n')
	file.write('                  <h3> Web Development </h3>\n')
	file.write('                </div>\n') ##service-item-title
	file.write('                <div class="service-item-desc">\n')
	file.write('                  <p>This is Web Development item</p>\n')
	file.write('                </div>\n') ##service-item-desc
	file.write('              </div>\n') ##service-item
	file.write('            </div>\n') ##column

	file.write('            <div class="col-md-4">\n')
	file.write('              <div class="service-item">\n')
	file.write('                <div class="service-item-icon">\n')
	file.write('                  <i class="fa fa-tablet fa-3x"></i>\n')
	file.write('                </div>\n') ##service-item-icon
	file.write('                <div class="service-item-title">\n')
	file.write('                  <h3> Mobile Apps  </h3>\n')
	file.write('                </div>\n') ##service-item-title
	file.write('                <div class="service-item-desc">\n')
	file.write('                  <p>This is Mobile Apps item</p>\n')
	file.write('                </div>\n') ##service-item-desc
	file.write('              </div>\n') ##service-item
	file.write('            </div>\n') ##column

	file.write('            <div class="col-md-4">\n')
	file.write('              <div class="service-item">\n')
	file.write('                <div class="service-item-icon">\n')
	file.write('                  <i class="fa fa-search fa-3x"></i>\n')
	file.write('                </div>\n') ##service-item-icon
	file.write('                <div class="service-item-title">\n')
	file.write('                  <h3> SEO Optimization</h3>\n')
	file.write('                </div>\n') ##service-item-title
	file.write('                <div class="service-item-desc">\n')
	file.write('                  <p>This is SEO Optimization item</p>\n')
	file.write('                </div>\n') ##service-item-desc
	file.write('              </div>\n') ##service-item
	file.write('            </div>\n') ##column

	file.write('            <div class="col-md-4">\n')
	file.write('              <div class="service-item">\n')
	file.write('                <div class="service-item-icon">\n')
	file.write('                  <i class="fa fa-pencil-square-o fa-3x"></i>\n')
	file.write('                </div>\n') ##service-item-icon
	file.write('                <div class="service-item-title">\n')
	file.write('                  <h3> UX Design </h3>\n')
	file.write('                </div>\n') ##service-item-title
	file.write('                <div class="service-item-desc">\n')
	file.write('                  <p>This is UX Design item</p>\n')
	file.write('                </div>\n') ##service-item-desc
	file.write('              </div>\n') ##service-item
	file.write('            </div>\n') ##column

	file.write('            <div class="col-md-4">\n')
	file.write('              <div class="service-item">\n')
	file.write('                <div class="service-item-icon">\n')
	file.write('                  <i class="fa fa-life-ring fa-3x"></i>\n')
	file.write('                </div>\n') ##service-item-icon
	file.write('                <div class="service-item-title">\n')
	file.write('                  <h3> Support  </h3>\n')
	file.write('                </div>\n') ##service-item-title
	file.write('                <div class="service-item-desc">\n')
	file.write('                  <p>This is Support item</p>\n')
	file.write('                </div>\n') ##service-item-desc
	file.write('              </div>\n') ##service-item
	file.write('            </div>\n') ##column

	file.write('					</div>\n') ##Row
	file.write('				</div>\n') ##Container
	file.write('			</div>\n') ##content-box
	file.write('		</section>\n')  ## End of services section


	file.write('		<!-- About -->\n')
	file.write('		<section id="about">\n')

	file.write('			<!-- About right side with diagonal BG parallax -->\n')
	file.write('			<div id="about-bg-diagonal" class="bg-parallax"></div>\n')

	file.write('			<!-- About left side with content -->\n')
	file.write('			<div class="container">\n')
	file.write('				<div class="row">\n')
	file.write('					<div class="col-md-4">\n')
	file.write('						<div id="about-content-box">\n')
	file.write('							<div id="about-content-box-outer">\n')
	file.write('								<div id="about-content-box-inner">\n')
	file.write('									<div class="content-title wow animated fadeInDown" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('										<h3> About Vesco </h3>\n')
	file.write('										<div class="content-title-underline"></div>\n')
	file.write('									</div>\n')
	file.write('									<div id="about-desc" class="wow animated fadeInDown" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('										<p>This is about the Vesco company.</p>\n')
	file.write('									</div>\n')
	file.write('									<div id="about-btn" class="wow animated fadeInUp" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('										<a class="btn btn-lg btn-general btn-blue" href="#work" role="button"> Our Work </a>\n')
	file.write('									</div>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n')
	file.write('		</section>\n') ## End of about section



	file.write('		<!-- Work -->\n')
	file.write('		<section id="work">\n')
	file.write('			<div class="content-box">\n')
	file.write('				<div class="content-title wow animated fadeInDown" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('					<h3> Our Work </h3>\n')
	file.write('					<div class="content-title-underline"></div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n') ## Content box
	file.write('			<div class="container-fluid">\n') ## container is a fixed width class whereas container-fluid will take the full width of the page
	file.write('				<div class="row no-gutters wow animated FadeInUp" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/1.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/1.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/2.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/2.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/3.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/3.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/4.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/4.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/5.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/5.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/6.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/6.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/7.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/7.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('					<div class="col-md-3">\n')
	file.write('						<div class="img-wrapper">\n')
	file.write('							<a href="img/work/8.jpg" title="Work Description Goes Here">\n')
	file.write('								<img src="img/work/8.jpg" class="img-responsive" alt="Work">\n')
	file.write('							</a>\n')
	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('				</div>\n') ## End of row
	file.write('			</div>\n') ## End of container
	file.write('		</section>\n\n\n') ## End of work section



	file.write('		<!-- Team -->\n')
	file.write('		<section id="team">\n')
	file.write('			<div class="content-box">\n')
	file.write('				<div class="content-title wow animated fadeInDown" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('					<h3> Our Team </h3>\n')
	file.write('					<div class="content-title-underline"></div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n') ## Content box
	file.write('			<div class="container">\n') ## container is a fixed width class whereas container-fluid will take the full width of the page
	file.write('				<div class="row wow animated FadeInUp" data-wow-duration="1s" data-wow-delay=".5s">\n')
	file.write('					<div class="col-md-12">\n')
	file.write('						<div id="team-members">\n')
	file.write('							<div class="team-member">\n')
	file.write('								<img src="img/team/team-1.jpg" class="img-responsive" alt="team member">\n')
	file.write('								<div class="team-member-info text-center>\n"')
	file.write('									<h4 class="team-member-name">Daniel Watrous </h4>\n')
	file.write('									<h4 class="team-member-designation">CEO</h4>\n')
	file.write('									<ul class="social-list">\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-facebook"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-twitter"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-google-plus"></i></a></li>\n')
	file.write('									</ul>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')
	file.write('							<div class="team-member">\n')
	file.write('								<img src="img/team/team-2.jpg" class="img-responsive" alt="team member">\n')
	file.write('								<div class="team-member-info text-center>\n"')
	file.write('									<h4 class="team-member-name">Sara Smith </h4>\n')
	file.write('									<h4 class="team-member-designation">Co-Founder</h4>\n')
	file.write('									<ul class="social-list">\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-facebook"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-twitter"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-google-plus"></i></a></li>\n')
	file.write('									</ul>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')
	file.write('							<div class="team-member">\n')
	file.write('								<img src="img/team/team-3.jpg" class="img-responsive" alt="team member">\n')
	file.write('								<div class="team-member-info text-center>\n"')
	file.write('									<h4 class="team-member-name">Steve Mike </h4>\n')
	file.write('									<h4 class="team-member-designation">Sr. Developer</h4>\n')
	file.write('									<ul class="social-list">\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-facebook"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-twitter"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-google-plus"></i></a></li>\n')
	file.write('									</ul>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')
	file.write('							<div class="team-member">\n')
	file.write('								<img src="img/team/team-4.jpg" class="img-responsive" alt="team member">\n')
	file.write('								<div class="team-member-info text-center>\n"')
	file.write('									<h4 class="team-member-name">Robert Hinay </h4>\n')
	file.write('									<h4 class="team-member-designation">Sr. Designer</h4>\n')
	file.write('									<ul class="social-list">\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-facebook"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-twitter"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-google-plus"></i></a></li>\n')
	file.write('									</ul>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')
	file.write('							<div class="team-member">\n')
	file.write('								<img src="img/team/team-5.jpg" class="img-responsive" alt="team member">\n')
	file.write('								<div class="team-member-info text-center>\n"')
	file.write('									<h4 class="team-member-name">Mike Tara </h4>\n')
	file.write('									<h4 class="team-member-designation">Sales</h4>\n')
	file.write('									<ul class="social-list">\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-facebook"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-twitter"></i></a></li>\n')
	file.write('										<li><a href="#" class="social-icon icon-gray"><i class="fa fa-google-plus"></i></a></li>\n')
	file.write('									</ul>\n')
	file.write('								</div>\n')
	file.write('							</div>\n')

	file.write('						</div>\n')
	file.write('					</div>\n')
	file.write('				</div>\n')
	file.write('			</div>\n')
	file.write('		</section>\n\n\n')








	file.write('<br>,br><br><br><br>,br><br><br><br>,br><br><br><br>,br><br><br><br>,br><br><br><br>,br><br><br>\n')

	file.write('		<!-- jQuery -->\n')
	file.write('		<script src="js/jquery.js"></script>\n') ## jquery needs to come before custom.js and bootstrap
	file.write('		<!-- bootstrap JS -->\n')
	file.write('		<script src="js/bootstrap/bootstrap.min.js"></script>\n')
	file.write('		<!-- WOW JS -->\n')
	file.write('		<script src="js/wow/wow.min.js"></script>\n')
	file.write('		<!-- magnific-popup JS -->\n')
	file.write('		<script src="js/magnific-popup/jquery.magnific-popup.min.js"></script>\n')
	file.write('		<!-- custom JS -->\n')
	file.write('		<script src="js/custom.js"></script>\n')
	file.write('\n')
	file.write('\n')
	file.write('	</body>\n')
	file.write('\n')
	file.write('\n')
	file.write('</html>\n')
	file.close()
