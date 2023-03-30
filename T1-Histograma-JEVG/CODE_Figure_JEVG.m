function createfigure(cdata1, yvector1, data1)
%CREATEFIGURE(cdata1, yvector1, data1)
%  CDATA1:  image cdata
%  YVECTOR1:  bar yvector
%  DATA1:  histogram data

%  Auto-generated by MATLAB on 02-Mar-2023 14:07:53

% Create figure
figure1 = figure;

% Create subplot
subplot1 = subplot(2,2,1,'Parent',figure1);
axis off
hold(subplot1,'on');

% Create image
image(cdata1,'Parent',subplot1);

% Create title
title('Imagen de Lena');

% Uncomment the following line to preserve the X-limits of the axes
% xlim(subplot1,[0.5 520.5]);
% Uncomment the following line to preserve the Y-limits of the axes
% ylim(subplot1,[0.5 304.5]);
box(subplot1,'on');
axis(subplot1,'ij');
hold(subplot1,'off');
% Set the remaining axes properties
set(subplot1,'DataAspectRatio',[1 1 1],'Layer','top','TickDir','out');
% Create subplot
subplot2 = subplot(2,2,2,'Parent',figure1);
axis off
hold(subplot2,'on');

% Create image
image(cdata1,'Parent',subplot2);

% Create title
title('Imagen de Lena');

% Uncomment the following line to preserve the X-limits of the axes
% xlim(subplot2,[0.5 520.5]);
% Uncomment the following line to preserve the Y-limits of the axes
% ylim(subplot2,[0.5 304.5]);
box(subplot2,'on');
axis(subplot2,'ij');
hold(subplot2,'off');
% Set the remaining axes properties
set(subplot2,'DataAspectRatio',[1 1 1],'Layer','top','TickDir','out');
% Create subplot
subplot3 = subplot(2,2,3,'Parent',figure1);
hold(subplot3,'on');

% Create bar
bar1 = bar(yvector1,'Parent',subplot3,...
    'FaceColor',[0.635294117647059 0.0784313725490196 0.184313725490196],...
    'EdgeColor','none');

% The following line demonstrates an alternative way to create a data tip.
% datatip(bar1,252,0);
% Create datatip
datatip(bar1,'DataIndex',252);

% Create title
title('Histograma ALGORITMO','FontWeight','bold','FontName','Arial Black',...
    'Color',[0 0 1]);

box(subplot3,'on');
hold(subplot3,'off');
% Create subplot
subplot4 = subplot(2,2,4,'Parent',figure1);
hold(subplot4,'on');

% Create histogram
histogram(data1,'Parent',subplot4,'BinMethod','auto');

% Create title
title('Histograma HISTOGRAM','Color',[1 0 0]);

box(subplot4,'on');
hold(subplot4,'off');
% Create line
annotation(figure1,'line',[0.519329896907217 0.520618556701031],...
    [0.985692015209125 0.0703422053231939],'LineStyle','--');

% Create arrow
annotation(figure1,'arrow',[0.289948453608247 0.289948453608247],...
    [0.599760456273764 0.505703422053232]);

% Create arrow
annotation(figure1,'arrow',[0.739690721649485 0.739690721649485],...
    [0.603562737642586 0.5]);

