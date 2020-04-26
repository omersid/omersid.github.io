<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>dissonance</title><style>
/* webkit printing magic: print all background colors */
html {
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
	
</style></head><body><article id="a5585370-2d91-4449-a955-5c09d733b7d8" class="page mono"><header><img class="page-cover-image" src="https://images.unsplash.com/photo-1470813740244-df37b8c1edcb?ixlib=rb-1.2.1&amp;q=85&amp;fm=jpg&amp;crop=entropy&amp;cs=srgb" style="object-position:center 50%"/><div class="page-header-icon page-header-icon-with-cover"><span class="icon">❌</span></div><h1 class="page-title">dissonance</h1></header><div class="page-body"><p id="cdfbc43d-8660-4f78-945b-707cce98d9d0" class="">I was looking to find myself wrong, misguided, or something else today. but something more pressing came up to stop me from torturing myself. it doesn&#x27;t matter if I&#x27;m right or wrong... unless I am doing it to others.</p><p id="8e03e2b6-0fd1-41ad-9ca3-bfe61c9a53b2" class="">
</p><p id="6d24a01c-a733-46f4-b128-d8133598ef0a" class=""><mark class="highlight-pink">maybe i&#x27;m wrong...</mark></p><p id="3cd62ccc-ecec-4212-bca3-be7e34a61039" class="">
</p><p id="af54e28b-aff4-4d92-955d-f69e0f80520f" class="">in order to be right, someone has to lose.</p><p id="1f6b2864-e982-4e8a-9e24-ed211ede63fd" class="">
</p><p id="aceba483-7c1a-428f-b13a-aa966ac043ba" class="">in order to be right about god, science, politics, or what ever else. someone else has to come to the conclusion that they were wrong, or were misguided, or made a little mistake somewhere. </p><p id="d569fbb1-c7c3-41c2-ba60-9415a55878ba" class="">
</p><p id="dc667c37-7970-4214-9a70-37c5ddd730a8" class="">Egoistically, it is not enough for one to feel right about something and not try to explain that to others. If i believe I&#x27;m right, is it not my duty to explain that to others. The foundational ideas of proselytization, the war for truth is deep in human nature, and has so  been exploited.</p><p id="d0ca3ff8-4c1a-4a79-ab4c-4e0dfb9e06cf" class="">
</p><p id="2024f423-5a00-4442-a772-ff8a5d04f445" class=""><mark class="highlight-pink">the only arbiter of truth is time, and math.</mark></p><p id="039c089a-f033-4c31-b117-339454ca89bd" class="">
</p><p id="5321fad7-d098-4207-a054-f28477aef74e" class="">most beliefs cannot be right. simply, because, you are rarely strictly right. more often you are just not wrong yet. Sadly, the real issue here is that humans don&#x27;t like being wrong which allows them to stay safe in their mind. if you wish to point out that someone is wrong, you will have to deal with being disliked. if you shatter the ground on which people stand (religion, or other centralized dogmatic belief), you must ask yourself — did you provide them another ground, before dropping them into the chaos of cognitive dissonance.</p><p id="4299aeea-b9fc-434b-8bf3-55f424e3a2fb" class="">
</p><p id="85cefba0-df90-42e8-9427-3b5dedbad0ff" class="">In plato&#x27;s Euthyphro we have socrates; engaging in an argument, and he asks his opponent to define &#x27;piety&#x27;. Socrates asks questions as though he does not know the answer, and has Euthyphro happily create the definitions, which he will be forced into contradicting. As a reprise, Socrates is sentenced to death in the Apology, for such things.</p><p id="78ac801b-2bfc-4076-a07e-42163ea980bf" class="">
</p><p id="acab5d6a-f33a-4b9a-9b4e-c3a7edc32f67" class=""><mark class="highlight-orange">theres a lesson in there</mark></p><p id="89ee93a4-6402-407c-8e3d-764936a5155d" class="">
</p><p id="b9420c0d-5380-4a47-a8f4-ee2417226a8e" class="">this brings me to the question, asked by those wanting to change something, make things better. probably asked by so so many people.</p><p id="6d7c35c6-d120-4c12-829c-355fb5c27b37" class="">
</p><p id="1e778075-22ed-4301-8124-bfa8b05410c7" class="">how do you change the world ? and maybe then the better question - how do you change the world without an absolute truth, (which is to say without exposing others to the consequences of being wrong — because you might be wrong).</p><p id="5c809501-4a6b-4b0f-8ca1-d22b1520cf4c" class="">
</p><p id="c5221f8a-e014-4e2e-906a-b6dc7ea2d6c4" class="">religions and various other &#x27;isms&#x27; seem to have basically implemented,  teaching infallibility, and then using dissonance to make sure people stay. of course they have their merits, but if something is easy to enter and hard to leave. how then is it not a trap — just like Socrates.</p><p id="0f3e3f32-0db7-488d-b6f4-37aa6db4cfa8" class="">
</p><p id="8fd1e560-c795-4b3a-afb7-fd48667e194a" class=""><mark class="highlight-pink">its not a trap if its right... </mark></p><p id="887984c3-0c65-45af-86ba-b02b5e8a1734" class="">
</p><p id="adeede3e-43e8-4d4e-b98f-ddee9c71babc" class="">anyways, back to simply changing the world. solving problems. We want to to be doing it without exposing vulnerabilities in society, without causing unrest, without people losing their faith in the world. </p><p id="5c4c291a-b67f-4cd3-a3c4-d096a03ce350" class="">
</p><p id="588c72b1-7b4e-4aef-8401-27f11e6d180f" class="">in order to fix america&#x27;s health right now. what pretty much would have to be done, is have the government, and doctors say yeah we&#x27;re sorry we didn&#x27;t realize our mistake when we said it XX years ago. But you should trust us now with this new information. that is obviously a bad fix.</p><p id="8bcff372-f3f6-48ef-8d55-22cff7292b79" class="">
</p><p id="3b470de6-70ce-4654-8086-61a813de150d" class="">sure rapid catastrophic changes can be good in the long run. but in thinking thats the best way, is definitely crazy. because it seems to neglect loss is harder to stomach, than gain.</p><p id="378e7222-3ce7-4b47-9c04-0ca0fdd94ccd" class="">
</p><p id="e47b64d1-76fc-4ba9-80c3-3ae9dc848d79" class=""><mark class="highlight-pink">to fix things, people have to want to be wrong...  </mark></p><p id="dc455902-a4d1-4a28-9e37-a907ffae067b" class="">
</p><p id="20b51dec-5c9b-4309-a2a4-f5460b8a098b" class="">with certain things its easy to want to be wrong. I want to be wrong about nutrition, urban planning, climate, economy because it&#x27;s easy to see things aren&#x27;t working as they might ideally, even without all of the random scientist&#x27;s confounding variables. </p><p id="ef5b6f10-7520-445c-8c8c-59b7d16e86b3" class="">
</p><p id="3f5aba32-59c7-4594-b5ef-1c97893ba590" class=""><mark class="highlight-red">if it something isn&#x27;t working; it doesn&#x27;t work.</mark></p><p id="e945d418-6bb6-4dfb-ad7e-21d97cf82cce" class="">
</p><p id="563b2e19-d3de-413d-a596-3be4b2ee2168" class="">If people don&#x27;t want to be wrong, usually they have something to lose, its quite human of them. So many people don&#x27;t seem to understand that. And I believe, all you can do to change their minds is plant seeds and let time nurture them slowly, carefully. If you don&#x27;t have time, maybe tell there there moms to tell them or something.</p><p id="a0c27159-86d2-4984-8080-36460aab5a7a" class="">
</p><p id="bba6779e-a937-4b12-8cff-7eae741b5aef" class="">Time will remove what is wrong. But by then you will be long gone. don&#x27;t try to fix the world out of pride, or revenge, its to murky. Don&#x27;t exploit someones ignorance.</p><p id="6c0cd2de-5dd1-4892-b824-085443551ca8" class="">
</p><p id="ed8ee9b9-2dc3-4b1d-a9cd-a14bf06d375e" class="">as i write this. I&#x27;m struck that there&#x27;s important nuance here. I&#x27;m only saying that to make me feel better to protect myself and feel safe. </p><p id="7dc7ecf6-f008-449e-b926-a699374de92e" class="">
</p><p id="33de90fd-8e10-471e-bb73-fdae0fd78d96" class="">so fine. Expose those who expose others. Call out those who cause the ruin of others. Ignorance is fine, I respect it as a noble solution to the problem of knowledge. But f**k those who cause ruin for others. Sometimes that ruin is so easy to see.</p><p id="6cb65438-19df-4ed3-93ff-a409c462eb5c" class="">
</p><p id="0ca52411-0508-4308-b206-d5171fdb0d99" class="">BUT D**N, we are back to loss aversion, how can i hurt people to help people. I must extend something better. in something like climate change, we have economic interests in fossil fuels conflicting with the planetary interest in solar panels. The issue is politics plays on two things, the working man who is employed by fossil fuels vs. the rich movie stars who speak for the climate. And in the same way, the poor affected by diminishing air qualities, crops, diseases vs some oil billionaire. Did either side extend solutions for the other ?</p><p id="8bbfa885-df4a-45cd-8e1f-bbe82b4fa083" class="">
</p><p id="6cc22ebc-afde-420b-ac68-0b6768b6e6dc" class="">God, stop giving us trolley problems and asking the majority to pull the lever. </p><p id="48059e06-1151-40b3-b603-96ef2d38470a" class="">
</p><p id="bd03cf07-7ed2-4ff4-9604-82c576e341b4" class="">the trolley problem is the worst. luckily this isn&#x27;t a philosophy textbook. you and nature simultaneously write the rules. remove the tracks, build another track, get the people off the tracks, stop the goddamn train. do them all at once, and just f**king hope you did it in time.</p><p id="8cfa56e6-7dd1-4e3d-994a-9ea5f64ed5d8" class="">
</p><p id="c3273ad5-c91e-4942-b25e-5e9c24f60008" class="">its not a game, and i don&#x27;t mean to game-ify it. but seriously, does anyone qualified to try even try these days. </p><p id="aa3ea781-06a5-4e60-a76b-8688dcb3e80b" class="">
</p><p id="c96fb6c5-94ba-4a51-87c9-c82c1ad0f1ef" class="">i really didn&#x27;t expect to get here. but IT&#x27;S TIME TO BUILD.</p><p id="3e3901ff-f5df-48d3-937e-5814865a978b" class="">
</p><p id="7662cb76-312a-4faa-be29-09db5945b543" class="">Sorry, I had to. Anyways, righting the ship. I don&#x27;t mean to provide non-practical statements. but I don&#x27;t have time to do everything myself. you shouldn&#x27;t care too much to show that you are right, that you have read more, that you have considered this and that and that. you will get to it eventually. don&#x27;t beat yourself up about it now.</p><p id="7eee5cea-439f-4291-9ab7-d1a887f85426" class="">
</p><p id="83e43e53-0792-42f0-917b-4f3aca5e1863" class="">remember you ain&#x27;t s**t and neither is anyone else.</p><p id="fd5ed3c1-5435-4a18-ad25-f3b542b37529" class="">
</p><p id="58722ba8-4924-4025-97c6-d941cdf42478" class="">if you wanted to be really smart, you&#x27;d have provided a constructive solution to the problem. people probably know it exists already.</p><p id="c9200f1f-6aa9-47cd-a1ae-8c36daeb45ed" class="">
</p><p id="19db59a7-4f78-446c-8bca-4ce3f4cbd068" class="">ultimately, you should be concerned with harm associated with knowledge. is not fixing this gonna hurt ? is fixing this gonna hurt ? </p><p id="7b0c63b7-fb12-46ef-b172-da3f265bf693" class="">and ultimately how can i make the fix not hurt ? this doesn&#x27;t have to be a zero sum game for anyone if you do things slowly, and carefully. </p><p id="0dea8674-ddce-416e-b6e5-960a1cbd9e4b" class="">
</p><p id="803ca634-a18f-4a98-8d0d-753b94c3cedd" class="">hopefully i answered my question...</p><p id="386237e1-a9e6-454a-b8b1-93689d516899" class=""> </p><p id="a5bf5cd3-7d69-4a63-8e61-62efae4a2440" class="">
</p><p id="004ccebf-b138-4066-a507-39e14ba99ebd" class="">
</p><p id="62b28e4a-083c-4f2e-9818-f94465b889c2" class="">
</p><p id="dfc6814b-e805-4c83-bdaa-db7a6068ab66" class="">
</p><p id="b9e5823a-37ba-4f8c-aa5c-5d81fb435b21" class="">
</p><p id="3ea98774-e31b-4e56-a5e3-95dbdfea567d" class="">
</p></div></article></body></html>