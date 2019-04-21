import React from 'react';
import PageTemplate from '../components/common/PageTemplate';
import Intro from '../components/Intro';

const MainPage: React.FC = () => {
    return (
        <PageTemplate>
            <Intro/>
        </PageTemplate>
    );
};

export default MainPage;