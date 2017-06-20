%%
results = [5 , 3.5 , 4 , 4 , 5 , 5 , 3 , 2.5 , 4 , 5 , 4 , 3 , 4 , 5 , 4 ; 5 , 4 , 5 , 4 , 5 , 4 , 2.5 , 3 , 5 , 4 , 5 , 3 , 4 , 5 , 4 ; 4 , 4 , 5 , 3 , 5 , 5 , 4 , 3.5 , 5 , 4 , 3 , 5 , 3 , 4 , 5 ; 5 , 5 , 4 , 4 , 5 , 5 , 2 , 4 , 5 , 5 , 5 , 5 , 4 , 4 , 4 ; 4 , 1 , 5 , 5 , 4 , 5 , 4 , 5 , 5 , 5 , 5 , 3 , 2 , 5 , 3 ; 4 , 3.5 , 3 , 2 , 3 , 3 , 5 , 5 , 5 , 4 , 2 , 5 , 3 , 1 , 4;];

%%

for index = 1:6
    figure('position', [0 0 1280 800]);
    result = results(index, :);
    histogram(result, 10);
    xlim([0, 5]);
    title(['Question ', num2str(index)]);
    xlabel('Score');
    ylabel('Frequency');
    
    set(findall(gcf,'type','axes'),'fontsize',50);
    set(findall(gcf,'type','text'),'fontSize',50);
    % Save data
    fig = gcf;
    fig.PaperPositionMode = 'auto';
    print(['./report/pics/q', num2str(index)],'-dpng','-r0');
    close;
    
end