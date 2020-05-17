---
title:  "Red Queen Blues + Happiness"
date:   2020-05-01 17:00:16 -0400
categories: thoughts
layout: post
permalink: /posts/red-queen-blues
---
<style>
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	text-indent: -1.7em;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, YuMincho, "Yu Mincho", "Hiragino Mincho ProN", "Hiragino Mincho Pro", "Songti TC", "Songti SC", "SimSun", "Nanum Myeongjo", NanumMyeongjo, Batang, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC', 'Noto Sans CJK KR'; }

.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC', 'Noto Sans Mono CJK KR'; }

.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, YuMincho, "Yu Mincho", "Hiragino Mincho ProN", "Hiragino Mincho Pro", "Songti TC", "Songti SC", "SimSun", "Nanum Myeongjo", NanumMyeongjo, Batang, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC', 'Noto Sans CJK KR'; }

.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC', 'Noto Sans Mono CJK KR'; }

.highlight-default {
}
.highlight-gray {
	color: rgb(155,154,151);
}
.highlight-brown {
	color: rgb(100,71,58);
}
.highlight-orange {
	color: rgb(217,115,13);
}
.highlight-yellow {
	color: rgb(223,171,1);
}
.highlight-teal {
	color: rgb(15,123,108);
}
.highlight-blue {
	color: rgb(11,110,153);
}
.highlight-purple {
	color: rgb(105,64,165);
}
.highlight-pink {
	color: rgb(173,26,114);
}
.highlight-red {
	color: rgb(224,62,62);
}
.highlight-gray_background {
	background: rgb(235,236,237);
}
.highlight-brown_background {
	background: rgb(233,229,227);
}
.highlight-orange_background {
	background: rgb(250,235,221);
}
.highlight-yellow_background {
	background: rgb(251,243,219);
}
.highlight-teal_background {
	background: rgb(221,237,234);
}
.highlight-blue_background {
	background: rgb(221,235,241);
}
.highlight-purple_background {
	background: rgb(234,228,242);
}
.highlight-pink_background {
	background: rgb(244,223,235);
}
.highlight-red_background {
	background: rgb(251,228,228);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(55, 53, 47, 0.6);
	fill: rgba(55, 53, 47, 0.6);
}
.block-color-brown {
	color: rgb(100,71,58);
	fill: rgb(100,71,58);
}
.block-color-orange {
	color: rgb(217,115,13);
	fill: rgb(217,115,13);
}
.block-color-yellow {
	color: rgb(223,171,1);
	fill: rgb(223,171,1);
}
.block-color-teal {
	color: rgb(15,123,108);
	fill: rgb(15,123,108);
}
.block-color-blue {
	color: rgb(11,110,153);
	fill: rgb(11,110,153);
}
.block-color-purple {
	color: rgb(105,64,165);
	fill: rgb(105,64,165);
}
.block-color-pink {
	color: rgb(173,26,114);
	fill: rgb(173,26,114);
}
.block-color-red {
	color: rgb(224,62,62);
	fill: rgb(224,62,62);
}
.block-color-gray_background {
	background: rgb(235,236,237);
}
.block-color-brown_background {
	background: rgb(233,229,227);
}
.block-color-orange_background {
	background: rgb(250,235,221);
}
.block-color-yellow_background {
	background: rgb(251,243,219);
}
.block-color-teal_background {
	background: rgb(221,237,234);
}
.block-color-blue_background {
	background: rgb(221,235,241);
}
.block-color-purple_background {
	background: rgb(234,228,242);
}
.block-color-pink_background {
	background: rgb(244,223,235);
}
.block-color-red_background {
	background: rgb(251,228,228);
}
.select-value-color-default { background-color: rgba(206,205,202,0.5); }
.select-value-color-gray { background-color: rgba(155,154,151, 0.4); }
.select-value-color-brown { background-color: rgba(140,46,0,0.2); }
.select-value-color-orange { background-color: rgba(245,93,0,0.2); }
.select-value-color-yellow { background-color: rgba(233,168,0,0.2); }
.select-value-color-green { background-color: rgba(0,135,107,0.2); }
.select-value-color-blue { background-color: rgba(0,120,223,0.2); }
.select-value-color-purple { background-color: rgba(103,36,222,0.2); }
.select-value-color-pink { background-color: rgba(221,0,129,0.2); }
.select-value-color-red { background-color: rgba(255,0,26,0.2); }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="d8b9c18f-9307-41cc-9a51-0d27c257626d" class="page mono"><header><img class="page-cover-image" src="https://images.unsplash.com/photo-1542222780-b06f7307d2c5?ixlib=rb-1.2.1&amp;q=85&amp;fm=jpg&amp;crop=entropy&amp;cs=srgb" style="object-position:center 48.150000000000006%"/><div class="page-header-icon page-header-icon-with-cover"><span class="icon">♥️</span></div><h1 class="page-title">—red queen blues &amp; happiness</h1></header><div class="page-body"><p id="3e0d7054-bb79-4e19-8759-ca79be2ca22b" class="">&#x27;<mark class="highlight-pink">The world is not enough.&#x27; </mark></p><p id="1fc3bec9-53b2-45b1-95ac-07a65d1b1bf1" class=""><mark class="highlight-pink">find happiness in the experience.</mark></p><p id="df35fbaf-f479-4f3a-a63f-e7cb72f9aba0" class="">
</p><p id="32a51fc4-4257-46c4-b8a6-bada04b32486" class="">The world — it could never be enough. Desire is deeply reflexive and self propagating. And let me say for good reason... Enter the <mark class="highlight-red">red queen.</mark> The beloved character from Wonderlands — who so thoughtfully is placed by Lewis Carroll. </p><blockquote id="e3e70124-6e5f-411a-9535-31b52ab9bb89" class=""><mark class="highlight-red">Now, here, you see, it takes all the running you can do, to keep in the same place.</mark></blockquote><p id="036cf6bf-85a4-4c49-b617-82a70044a2a0" class="">The Red Queen is our &#x27;hypothetical&#x27; adversary; a recurring foe: requiring societies to continually adapt and evolve, or face extinction.</p><p id="0efdefca-6662-4e95-a18d-d81226a241dd" class=""> </p><p id="48546d13-cbd7-4e67-89cb-4b22bc2d00dc" class="">Even if we were &#x27;happy&#x27; or &#x27;content&#x27; thousands of years ago, humanity still advanced to today. Jared Diamond posited that the transformation from &#x27;hunter-gatherer&#x27; was our worst mistake. Maybe people could have been happier, possibly even less vulnerable to large scale extinction, had we not. However, this is flawed, because it forgets that small-scale (individual, local) extinction is far greater motivator. </p><p id="747a6b03-5972-4c6a-bc73-e221b996b633" class="">
</p><p id="21f7b123-7fc2-45d6-a8c1-98b7e4ccd509" class="">The moment that one society gained any advantage while farming (or whatever); other societies had to adapt or gain that advantage, else face &#x27;possible&#x27; extinction. The red queen applies to human struggles against other humans, animals, pathogens, and ultimately the universe. We are always, and will always be &#x27;vulnerable&#x27; to something. Societal feeling of invulnerability is usually a prophecy for demise. Very few things are &#x27;invulnerable&#x27;. If you are beginning to be cynical about the world,stop being lazy, I&#x27;ll get to connecting happiness back.</p><p id="97ab76e6-e083-4948-a22c-6c545c2e20a4" class="">
</p><p id="5ab54d5a-9e4a-4bbe-91a9-854bd5812142" class="">Today, there have many &#x27;red queens&#x27;. Humanity has &#x27;rna viruses&#x27; and &#x27;meteors&#x27;, &#x27;soviet/harvard intellectuals&#x27;, &#x27;(most) nobel prize winners in economics&#x27;, &#x27;mercury poisoning&#x27;, &#x27;organized religion&#x27;, &#x27;slip-n-slides&#x27;. </p><p id="440ac7b6-749f-47e4-a469-f865a55f641d" class=""><mark class="highlight-red">These are things that have evolved to destroy us.</mark></p><p id="1a71e8c5-0ccb-48e8-ab50-67b10b324c51" class="">On a slightly smaller scale, India has &#x27;china&#x27;, China has &#x27;freedom&#x27;, U.S.A has &#x27;vegetable oils&#x27; &#x27;al-qaeda&#x27;, &#x27;chiiina&#x27;. Democrats have &#x27;jeff bezos&#x27; and &#x27;patriotism&#x27;, republicans have &#x27;women&#x27; and &#x27;logic&#x27;, libertarians &#x27;government&#x27;. </p><p id="ca2305c0-ec47-413f-9e43-c62b956517ee" class="">Michigan has &#x27;Ohio&#x27;, Texas has &#x27;U.S.A&#x27;, California &#x27;milk from cows&#x27;. Doctors have &#x27;preventative medicine&#x27;. Engineers have &#x27;nature&#x27;, lawyers have &#x27;the law&#x27;. Amazon has &#x27;any physical store&#x27;, Netflix has &#x27;productive uses of one&#x27;s time&#x27;. The NRA &#x27;knives&#x27;, AARP &#x27;teens&#x27;. </p><p id="8cf617e5-80cc-4b1e-9b8e-9848eaf2ac28" class="">And... Bill Gates has &#x27;mosquitoes&#x27;, Donald Trump has &#x27;self-awareness&#x27; and finally you have &#x27;me&#x27; and ... ... you have &#x27;you&#x27;.</p><p id="57fb821f-35d4-4f61-b1d3-4ceb4a99e3fa" class="">Anyways... the point is (imaginary or not) people often find or have some &#x27;enemy&#x27; to fight against in some endless struggle. At the largest scale all of humanity is fighting against extinction. —And again, I&#x27;m not trying to take away your happiness.</p><p id="fb0bf798-214b-403c-aa18-64ed812e113f" class="">
</p><hr id="e36c764d-f880-48dd-b652-8cd23c02ad7f"/><p id="4af80242-b241-4523-8a72-80f075c916eb" class=""><mark class="highlight-pink">&#x27;happy + free&#x27;</mark></p><p id="42558db2-65f6-45a4-b28f-574b125d67ca" class=""><mark class="highlight-red">so, this is going to be a long essay. I&#x27;m getting toward a goal of wanting all people to have the opportunity to be happy and free. </mark></p><p id="159e1c5f-208b-4f86-84c9-7bde03826e7c" class="">This is a topic thats been on human minds since we gained consciousness. Sadly, this knowledge was not necessarily cumulative. Physics and Medicine gain understanding with time, Happiness is different. I wholeheartedly agree that the principles for happiness are available, and have been available for a long-long time. The only thing is that the &#x27;instructions&#x27; are not necessarily easily translatable across time. Religions, philosophies, culture are the primary purveyors of this material and they definitely work for some. But, they have obviously become less potent in our world. Maybe for many reasons. Today more knowledge and comfort is accessible to people than ever before. Our philosophies / religions seem built for scarcity, ignorance, non-connected society.</p><p id="5dafb697-827a-4649-bd7e-fced7b5c96fe" class="">people still use them and thats perfectly fine; they are all accomplishing things... but it is evident that there are problems.</p><p id="31f57933-09e7-49f1-bf8c-2f65eeea33b0" class="">
</p><hr id="04f902cd-1a87-4e1d-b456-684f8e6a6ab9"/><p id="7ba799c0-8c5c-415d-a9a4-a9398e1d9a58" class=""><mark class="highlight-pink">&#x27;love of life&#x27;.</mark></p><p id="6f425aef-e926-45d9-bca9-15a42bacea6e" class="">the principles of happiness are mostly known. analysis of any prominent religion, philosophy, and we find elements which are conducive to happiness. However, I am unable to take happiness, at the cost of freedom, knowledge, tolerance, ignorance. Which is where I take issue. Religion (centralized)(non-local) is built on &#x27;red-queen&#x27; &#x27;us-them&#x27; struggles as well as professed ignorance to prop it up, no different from communist china. 🧐</p><p id="e7e03824-0244-41bc-b06e-f300ab26fb96" class="">Here&#x27;s some foundational ideas for societal happiness.</p><p id="6c395c57-a925-4f0c-ac7c-1a7b8d8fe804" class=""><mark class="highlight-gray_background">&#x27;antifragile&#x27;, &#x27;skin in the game&#x27;, &#x27;red queen&#x27;, &#x27;eternal&#x27;, &#x27;experience&#x27;, &#x27;zen&#x27; (dhyana, flow), &#x27;love&#x27;.</mark></p><p id="f4e549e1-c6f8-41b9-be1e-aaae0612d558" class="">—There are always exceptions. But here are the things I&#x27;m thinking about—</p><p id="5ca37bcc-ee32-4804-a51b-d25824cebf6e" class="">Happiness is at it&#x27;s core &#x27;love of life&#x27; — contentness with experience. The idea is you can want things deeply (sure), but your happiness wasn&#x27;t predicated on getting there (necessarily), its about enjoying or accepting the struggle or whatever. (you can control it mostly)</p><p id="1d4664ed-8306-44a9-a82c-6bb2ed6b9157" class=""><mark class="highlight-gray_background">If you are aiming to be happy tomorrow, you won&#x27;t be happy tomorrow.</mark></p><p id="8b3f8913-1332-4b87-bd8f-a4908b0c5f86" class="">Other principles. Happiness is antifragile (or at least robust) to the one&#x27;s surroundings. It is difficult to displace, perturb, and mostly is amenable to variations. The Red Queen / endless struggle / desire type issue does not invalidate it, or make it impossible. It strengthens it.</p><p id="c7dcf4ae-9ba8-4ce9-86ba-04f31ae03392" class=""><mark class="highlight-gray_background">Happiness should &#x27;not&#x27; be at the expense of others. </mark></p><p id="9ebe9bb2-f608-4a75-bc40-e28017b6835e" class="">If your happiness is predicated on someone else&#x27;s suffering or whatnot, that&#x27;s not good. Happiness should breed happiness. </p><p id="c6205659-dc30-4ddd-b0e1-2b4b9622a39a" class=""><mark class="highlight-gray_background">No happiness without tolerance</mark></p><p id="ae2dcab7-d53d-441c-8164-65c5875d8334" class="">Ultimately, happiness is an individual experience. It can be &#x27;taught&#x27; but must be sought. There are commonalities given that we are all &#x27;human&#x27;, and subject to same nature. Certain conditions in the world allow for happinness to occur more naturally.</p><p id="a3a72e58-da04-408b-8805-bac436be44b5" class=""><mark class="highlight-gray_background">the current &#x27;west&#x27; is non conducive to happiness, and will implode at the cost of human rights and freedom for everyone. </mark></p><p id="40d711e1-0248-474d-94f9-cdefa89b812e" class="">whatever is being done in the U.S.A et al. isn&#x27;t working at scale. Even if I&#x27;m anecdotally speaking about perceived social problems without understanding if they were present before. Suicide rates don&#x27;t lie. Also theres alot of expressed symptoms of unhappiness — contrived internal &#x27;red-queen&#x27; battles, which have no purpose except to give people purpose. Ultimately, I don&#x27;t believe in just assuaging the symptoms, but also focusing on causes. I believe in liberte egalite fraternite and what not. And will not let the west commit suicide, and be eaten up at the cost of freedom.</p><hr id="4f70ca9c-9257-4843-aaea-3a95b0941759"/><p id="63bf4f8f-c854-439b-b38e-914c0d94212d" class=""><mark class="highlight-pink">Happiness at Scale.</mark></p><p id="56fb11fb-d102-4989-9468-3fe90d87c975" class="">We have more &#x27;things&#x27; than we ever had. We can travel the world, and basically do anything. We can talk to people across vast distances. We have little shortages of food or water. Computers compute things for us. Doctors can heal most injuries. Basically... scarcity of most neccesities is non existent. So... what does that tell us (if we didn&#x27;t know already)... here it comes ... wait for it ... happinness isn&#x27;t external.</p><p id="8e30e6e8-cbcc-416e-9cdd-8bdaa3fa38e0" class="">
</p><p id="af03864c-8442-4b6e-9a4a-e65ea294d446" class="">
</p><p id="02ab30ca-2dc1-4726-8c8e-4e89bdc6a824" class="">— alright so this article needs more inspiration so i&#x27;ll be back later.</p><p id="20d9112f-2b2f-499a-b20e-a6c2347c040b" class="">... i&#x27;m not done lol ... to be continued</p><hr id="845fef73-cfdd-40c2-9b30-8748a90afec7"/><p id="55718dec-e7e1-4b3f-8e13-bcb5f8e44175" class="">[Primary reading list for this essay]</p><p id="3d52bb88-551b-4c7d-9b75-c4786b5dcf12" class="">-Flow (the psychology of optimal experience)</p><p id="4f8c9496-17b2-4df5-a525-4681bd44aff3" class="">-Incerto</p><p id="807ba440-fea4-4269-88f0-e3735d457c61" class="">-Bhagavad Gita</p><p id="b43de099-f281-499d-92f0-c0c05e6b51a2" class="">-Zero to One.</p><p id="65dba9ce-aa9f-48a3-a406-f339c1b8b1d7" class="">-Meditations</p><p id="b9ff59b4-8b76-4152-841f-6470b0624133" class="">-Letters from a Stoic</p><p id="c12491ea-65e5-4907-89a6-72d7d5173f2f" class="">-Deep Nutrition</p><p id="51f7ca69-a6c8-44e5-9bc0-ea7a436c62da" class="">-Guns Germs Steel</p><p id="6195b1a4-1814-4cd4-b6dc-ab331ccc75e6" class="">
</p><p id="ad3e8e30-2c77-4bee-829a-0ffd298b7bbd" class="">
</p></div></article>