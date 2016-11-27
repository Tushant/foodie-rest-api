import React, {Component} from 'react';
import _ from 'lodash';

const Menu = ({restaurant}) => {
  const veg = _.filter(restaurant.meal, (meal) => {
        return meal.meal_category.name==='veg';
    });
    const nonVeg = _.filter(restaurant.meal, (meal) => {
        return meal.meal_category.name==='Non-veg';
    });
  return(
    <div>
        <ul className="list-group veg">
                  Veg
                  {
                      _.map(veg, (meal) => {
                          return <li className="list-item-group" key={meal.id}>{meal.name}</li>
                      })
                  }
          </ul>
          <ul className="list-group">
              Non-veg
              {
                  _.map(nonVeg, (meal) => {
                      return <li className="list-item-group" key={meal.id}>{meal.name}</li>
                  })
              }
          </ul>
    </div>
  );
}

export default Menu;
