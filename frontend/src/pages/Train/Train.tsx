
import React from 'react';
import './styles.scss';
import Iframe from 'react-iframe';

const Train = () => {
  return (
    <div>
      <Iframe url="https://ex.semenushkin.ru/train/"
              width="100%"
              height="600px"
              display="block"
              position="relative"/>
    </div>
  )
}

export default Train
  