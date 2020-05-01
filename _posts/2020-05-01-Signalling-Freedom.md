---
title:  "Signaling Freedom ?"
date:   2020-05-01 17:00:16 -0400
categories: thoughts
layout: post
permalink: /posts/signalling-freedom
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

a,
a.visited {
	color: inherit;
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
	
</style>
<body><article id="b8882c31-f1da-4eab-815f-5e47377e1a05" class="page serif"><header><img class="page-cover-image" src="https://images.unsplash.com/photo-1526041092449-209d556f7a32?ixlib=rb-1.2.1&amp;q=85&amp;fm=jpg&amp;crop=entropy&amp;cs=srgb" style="object-position:center 50%"/><div class="page-header-icon page-header-icon-with-cover"><span class="icon">🎆</span></div><h1 class="page-title">Non-Costly Signalling</h1></header><div class="page-body"><p id="d59fb0b2-c775-4964-af4b-e0ee4bf2aacf" class=""><mark class="highlight-red">all the world is a stage and all my life is a heuristic.</mark></p><p id="18aa6dee-303f-4f6f-8d6e-a74470bdd8c0" class="block-color-red">i yearn for the world with equality, but must with great pain settle that I make it fair.</p><hr id="0f958c60-230b-418f-8a99-c9d0e42ce5af"/><p id="46365b6c-c148-4abb-b2ef-acbd1ea26747" class=""><code>there isn&#x27;t enough olive oil in the world for all of us.</code> </p><p id="5737007d-2100-4eee-b2e8-94c5ec8063e4" class=""><code>true freedom is expensive</code> <code>bless those who have made it cheaper</code></p><p id="d95f3240-acfc-414a-9e32-dd4da604f4a2" class="">
</p><p id="c4c1f4bf-7697-4882-b0f8-2ee2f8a4cd58" class="">I began this note to evaluate signaling theory, virtue signaling, skin in the game and whatnot. And found I could not evaluate them without breaking them.  That with everything that I write about — only heuristics are given.</p><p id="e0254d63-0809-471a-9933-9095ce3d1c55" class="">Signalling theory is a framework for understanding communication between individuals in th light of evolution usually. The premise is generally that individuals are communicating their evolutionary fitness to others. With humans, we have a bit more complex issue  because we get to &#x27;think&#x27; and can  &#x27;choose&#x27; things, whereas we assume animals cannot.</p><p id="cc22ad75-20de-4e2c-874b-9e86a602f2b7" class="">... so still pretty easy to see some signalling. </p><div id="697740e5-bbd8-4c8e-b3fe-3256a639aced" class="column-list"><div id="27e6707f-20f1-4cb4-bda5-653536baea6c" style="width:50%" class="column"><figure id="14d545d4-87cd-40b8-83df-ec3c77f7187e" class="image"><a href="/images/frog.png"><img style="width:240px" src="/images/frog.png"/></a></figure></div><div id="7368c59d-0fdb-44fa-84c1-51b261ef477c" style="width:50%" class="column"><figure id="125fab90-68cf-4f46-bf15-f5f7d57007d3" class="image"><a href="/images/peacock.png"><img style="width:336px" src="/images/peacock.png"/></a></figure><p id="bc0b5a77-0410-4e84-84a4-31e5be3c8f58" class="">Dangerous frogs, and pretty birds.</p></div></div><p id="9a0bc430-b2a4-40b1-862f-09763f824862" class="">In humans, maybe at base we are signalling reproductive fitness, but sadly once we figured that out, things got worse. Nevertheless, fitness is best considered at system level. I cannot super rigorously evaluate an individuals fitness, without assuming things about the world we live in.  Anyways, I don&#x27;t truly believe that  everything is just reproductive fitness for humans... or maybe<div class="indented"><p id="1800c399-a85b-4d0f-bdec-0a66ed0b02d9" class="">
</p></div></p><figure id="70e6945b-b19a-41a2-aba9-87a375e06cb3" class="image"><a href="/images/allsex.png"><img style="width:500px" src="/images/allsex.png"/></a><figcaption>                    There is no such thing as a product. Don&#x27;t ever think there is.</figcaption></figure><p id="ba3ee823-e693-4b93-b13d-83ed8ef652f6" class="">
</p><p id="293db6aa-4338-477f-95da-c45cdd23e34b" class="">The source of this post was this article below, and a bit of reading on the Veblen&#x27;s Leisure class, and signalling.</p><figure id="8ecdb7c2-b7fc-429f-a301-1c85920ee3dc"><a href="https://quillette.com/2019/11/16/thorstein-veblens-theory-of-the-leisure-class-a-status-update/" class="bookmark source"><div class="bookmark-info"><div class="bookmark-text"><div class="bookmark-title">Thorstein Veblen&#x27;s Theory of the Leisure Class-A Status Update - Quillette</div><div class="bookmark-description">I was bewildered when I encountered a new social class at Yale four years ago: the luxury belief class. My confusion wasn&#x27;t surprising given my unusual background. When I was two years old, my mother was addicted to drugs and my father abandoned us.</div></div><div class="bookmark-href"><img src="https://i0.wp.com/d24fkeqntp1r7r.cloudfront.net/wp-content/uploads/2019/05/16053149/cropped-Q-1.png?fit=192%2C192&amp;ssl=1" class="icon bookmark-icon"/>https://quillette.com/2019/11/16/thorstein-veblens-theory-of-the-leisure-class-a-status-update/</div></div><img src="https://i0.wp.com/d24fkeqntp1r7r.cloudfront.net/wp-content/uploads/2019/11/16205527/PCKX6B.jpg?fit=1500%2C1000&amp;ssl=1" class="bookmark-image"/></a></figure><p id="ccf405d5-80b9-41c6-bf32-378888ed92b8" class="">
</p><p id="135f5ff0-a7be-4ea1-a0f0-c04af315b1dd" class="">My feeling was mixed. The ideas presented by Veblen presented that status signalling by the leisure class (wealthy folks et al.) would cause problems for the lower classes, and society in general.  It seems some ideas have merit, but I couldn&#x27;t back everything up.  The ideas presented would suggest given some world with two classes. The class with more freedom, money, etc, would attempt to distinguish themselves from the other by doing things only they could do. So maybe one might have had a car, or servants or something back then.  But eventually, the main idea presented is that when non-leisurers would attempt to emulate this, they would some how cause ruin for themselves, because usually these things require freedom and optionality at some base level. My conclusion from this argument was that freedom is irreplaceable; that you should not <strong>blindly</strong> want the trappings come with it; that&#x27;s a false god. </p><p id="0d181b61-2c32-4974-9bc9-22edd46d49d0" class="">...now despite circularity I explain my argument</p><p id="21cb76ba-7208-4498-980f-d7bff7f95f00" class=""> </p><blockquote id="c4340c60-8186-404a-b026-e884b1a2e4eb" class="">In order to gain and to hold the esteem of men it is not sufficient merely to possess wealth or power. The wealth or power must be put in evidence, for esteem is awarded only on evidence. - Veblen</blockquote><p id="5b86f756-b13e-4f6e-944a-63485ba4dd0a" class="">
</p><p id="71518faf-7d81-4db1-ad97-0415ae595ea4" class="">So maybe thats true... what might be examples of this. I&#x27;m afraid to say that even though I don&#x27;t believe the theory completely; the phenomena is evident. I understand this could be due to some human bias, but we shall see.</p><p id="5a2939cd-a83b-4ca7-aaf3-d91b580182a7" class="">
</p><p id="46433fb6-215a-4015-b7eb-06aeafdb846d" class="">The wikipedia article on the Leisure class provides a couple of examples, but I don&#x27;t see the merit in all of these, because I&#x27;m not sure how to define the <code>wealthy</code> <code>leisure</code> class for each case. Anyways...<div class="indented"><p id="fbed14ca-d534-4608-8fb8-d10caae87491" class="">Organized Religion. Social Etiquette. Sports. Housewife</p></div></p><p id="d647253c-af2a-4c26-90a2-56b9dcaa6a4e" class="">And here are some modern examples.<div class="indented"><p id="f773c42b-22b9-4127-9579-caf89e5b918c" class="">Sexual Norms —&gt; Reduced Marriage Success</p><p id="c46bf902-d045-4bea-a6d1-225290407548" class="">Technology —&gt; Social Problems</p><p id="4e277b57-1d2f-4e25-a9f7-59ddb1735e8c" class="">Modern Scientific Diet —&gt; Obesity</p><p id="0becf7b9-3212-4276-bd3b-c4a1566df128" class="">Higher Education —&gt; Debt</p></div></p><p id="f21afdd6-17f6-4500-a7cf-0b32d1932e4d" class="">The leisure class doesn&#x27;t evade these problems completely and I&#x27;m not completely sure that the <code>leisure class</code> caused all these problems. I&#x27;d probably have to resend us back to being hunter gatherers before I can get around the fact that the more technology and society — the more inequality. Technology and Society concentrate power, but not without merit.</p><p id="bf5cbc89-ea9f-43cc-85e3-2e03e83b1b98" class="">My main point is that at some point the &quot;rich&quot; get to ignore the problems, because they were free to start with. The technology case is epitomized by silicon valley, who espoused technological integration in human life, to discover later that no they didn&#x27;t want their kids using iPads at their private schools after making sure that every public school had one. Identifying this phenomenon is  useless: it is known.</p><p id="2fa836be-d96e-450d-b70d-bd2830238fc5" class="">
</p><blockquote id="32ca1251-6940-49c7-bf69-9948783195a9" class="">things can be made cheap. but freedom is still expensive</blockquote><p id="e37c033e-cd6a-4c6c-a473-06b597db9251" class="">
</p><p id="3d168244-6e52-4f27-b9a6-97bbaedcde6c" class="">The Quillete article I referenced, also talks about <code>luxury beliefs</code> . Today material goods aren&#x27;t expensive.  No matter the social class, you have some more conveniences that previous generations did not. The fact is that now we made most neccessities cheap, even if there are expensive versions. Things aren&#x27;t freedom anymore. </p><p id="97fb4f8f-80ca-4afd-a96f-3a9103c6042d" class="">Freedom is a feeling — a level of control of whatever world you&#x27;re in. </p><p id="233fed67-972d-4bbb-b893-fadff311bb0c" class="">Today, we have luxury beliefs to distinguish people with freedom. The entire idea disgusts me. Luxury beliefs are things only rich people get to have; usually because they sound good theoretically and won&#x27;t  hurt them too much. Legalize all the drugs, no vaccinations, open borders, &#x27;privilege&#x27; ... Theres less skin in the game for rich people, because they have savings.  And for the non-leisure class these things maybe hurt or maybe don&#x27;t hurt (can depends on scale). </p><p id="8ef1e364-70f1-4362-b3d9-16cc55055914" class="">So as usual... I&#x27;m at a point where I find a problem. I don&#x27;t like the cause, and I dont truly know the solution.  —- Freedom is better and its expensive. Making it cheap is an ordeal.</p><hr id="f764442a-f923-496e-bf8c-ac53cf06e80b"/><p id="ffe2922b-b5c6-4d2a-b931-a8991e2c45b1" class="">When I originally began this article. I was attempting to show my disgust at signalling without cost. So I took a walk... and I smoothed that over. Signalling was mostly disgusting because I didn&#x27;t like who/what was signalling.  Also sometimes signaling isn&#x27;t even signaling its just doing what you&#x27;d normally do, but people taking it out of context.</p><p id="dec965b1-45ae-4bc4-b7eb-b50cd844a7b9" class="">Signaling is human nature. We need to express proof of work in whatever it is without wasting time. We want to <strong>trust</strong>, and this is a nice way to do it. Signaling is a heuristic — embodying I don&#x27;t know if this is the perfect idea, but from the look of it its pretty good. Aesthetics, Risk, Credentials whatever — they each attempt to show something, without showing it.</p><p id="cd19096d-62ec-432a-bb5b-a6a24421ab31" class="">
</p><p id="50f325ed-a886-4cce-8035-2a2e2815c75f" class="">Freedom is so easy to fake. Too easy to fake. Just copy the people, institutions, that are the <code>best</code> and we are good. Copy Harvard, influencers, wealthy, whatever...</p><p id="832e1248-d161-46d1-adb6-1c1a48d0f7f8" class="">
</p><p id="c4473d82-4d29-4ba1-bb8b-bb88d33e6165" class="">I am going to criticize and applaud signaling. Everything we do is a signal. This article is a signal, my thoughts are a signal, the clothes I wear, the health I keep. Its just communication. Just beware of it. I can&#x27;t not signal at some point. I can&#x27;t tell anyone to stop trying to look free. Looking free sometimes just means you&#x27;re free. Form follows function. </p><p id="7638859b-bb44-45ec-9cd0-d975501c2c15" class="">
</p><p id="26e49f7b-3093-4fdb-94f8-cae5cf824650" class="">The entire point of this is that even beliefs today are luxury goods. I shan&#x27;t be telling you anything. Signalling is so weird, very subjective when it involved humans. Silicon Valley got free enough, they realized they should wear drab clothes. Thats a signal (maybe they didn&#x27;t want it to be), everyone may not respond the same way.  </p><p id="c6153475-8e98-46e4-9a2b-7c54e6b12bf5" class="">
</p><p id="39fdb9d4-fb04-41f8-a0fe-f22db50367ef" class="">BEWARE OF SIGNALING... its too easy to fall for, because it makes sense sometimes.  Or maybe don&#x27;t beware of it.  Do what you want to do. Just be careful. :) </p><hr id="2ee9928d-3581-4025-a757-96d752426b20"/><p id="633d176f-a199-4702-b233-30be835dee9e" class="">Now...I couldn&#x27;t find my way to the idea of costly signaling. But it&#x27;s important because when things have risk — you are more believable.</p><p id="a20c682d-3b36-479c-9f9d-ba563646d848" class="">The ability to take risks itself implies you are decently free. You have money, or are healthy, or are whatever. Either that or you have nothing, no liabilities to look after. This is it.  A billionare can give away 99% of his wealth, you cannot. For the leisure class the risk is always comparatively small — so they can do whatever they want. They can start a business, or pay for college, or whatever. This is not to say risk is required to be anything. Just because it was easier for someone to do something, doesn&#x27;t mean they didn&#x27;t do it. When billionaires become politicians, they are scrutinized heavily, but just cause they can buy things to get elected doesn&#x27;t mean you have to choose them. Sure they have influence, you just wish the influence was on your side.</p><p id="aa2f059a-670b-4c20-9eec-905c8b76f6c7" class="">You don&#x27;t need to be doing whatever, you&#x27;d just like the option.</p><hr id="2d7902bc-0987-42d3-806d-98902ccba81d"/><p id="41477e6c-2646-4480-a1f9-81feba404fb8" class="">Signaling virtue signaling is also virtue signaling. (my initial problem in writing this —&gt; which i outgrew)</p><p id="1cec08c4-68fa-4b24-9d21-db746afe1592" class="">
</p><p id="bc7592ac-8b1b-4aa6-9b05-31ae7e9d9419" class="">Of course that isn&#x27;t helpful information. Very impractical, and quite indefensible. People do signal things which are harmful to signal. And signaling that they are being harmful is fine, potentially its <code>privileged</code> or whatever or maybe it makes you look better. But its fine.</p><p id="7b337b93-ba5f-4f3f-b369-0e8c0cd4058e" class="">The truth is everyone does it. Just look for the BS.</p><p id="c41a1e64-d980-46b0-a588-97f55ed29576" class="">
</p><p id="022629d3-ad2f-4e1c-8cc4-c19650c32ae2" class="">if someone advocates doing something they personally wouldn&#x27;t do. go get em... or  run em out of business. also if they aren&#x27;t eating their own sauces, don&#x27;t eat their sauces. </p><p id="29a95c13-1c2d-49bc-8b32-e4f326c21ad5" class="">if Silicon Valley ain&#x27;t using their own tech ... if  some big food execs ain&#x27;t eating their doritos  ... </p><p id="f6af187a-80dd-4a7d-be95-b446f4a572bc" class="">
</p><p id="c5fe4f0a-c43c-4430-b019-7c7099405abd" class="">Mostly — understand that if someone <code>free</code> does something. you want to be free and do that thing. not just do that thing. doing that thing may or may not be good for you in your situation.</p><p id="dd375e70-9ce4-4fa6-92bd-2c0e17425751" class="">
</p><p id="0d6d0b9e-f4d9-42e1-8606-45cccd9e0a2f" class="">
</p></div></article></body>